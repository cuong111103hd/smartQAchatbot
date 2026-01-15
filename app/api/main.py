from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.rag.embeddings import EmbeddingModel
from app.db.vector_store import FAISSVectorStore
from app.rag.retriever import Retriever
from app.rag.context_builder import build_context
from app.rag.generator import RAGGenerator
from app.rag.ollama_client import OllamaClientCLI
import os 

VECTOR_PATH = os.getenv("VECTOR_STORE_PATH", "app/data/processed")

app = FastAPI(title="PDF RAG QA with Ollama")

# Load once at startup
embedder = EmbeddingModel()
vector_store = FAISSVectorStore(dim=384)
vector_store.load(VECTOR_PATH)
retriever = Retriever(vector_store, embedder)
ollama_client = OllamaClientCLI(model="qwen2.5:7b")
generator = RAGGenerator(ollama_client)


# Request model
class AskRequest(BaseModel):
    question: str
    top_k: int = 5


@app.post("/ask")
def ask_pdf(req: AskRequest):
    try:
        # 1. Retrieval
        retrieved_docs = retriever.retrieve(req.question, top_k=req.top_k)
        if not retrieved_docs:
            return {"answer": "No relevant information found in PDF."}

        # 2. Build context
        context = build_context(retrieved_docs)

        # 3. Generate answer
        answer = generator.generate(req.question, context)

        return {
            "answer": answer,
            "context_used": [ {"section": d["metadata"]["section"],
                               "page": d["metadata"]["page"],
                               "text_preview": d["text"][:200]} 
                              for d in retrieved_docs ]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
