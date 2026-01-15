from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title = "Smart Domain QA Bot",
    description = "Advanced RAG-based QA system over PDFs",
    version = "0.1.0"
)

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status":"ok"}