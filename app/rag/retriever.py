from typing import List, Dict
from app.db.vector_store import FAISSVectorStore
from app.rag.embeddings import EmbeddingModel

class Retriever:
    def __init__(self, vector_store: FAISSVectorStore, embedder: EmbeddingModel):
        self.vector_store = vector_store
        self.embedder = embedder

    def retrieve(self, query: str, top_k = 5)-> List[Dict]:
        query_embedding = self.embedder.embed_texts([query])
        results = self.vector_store.search(query_embedding, top_k = top_k)
        return results
    
    