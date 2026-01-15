from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "PDF uploaded (not processed yet)"
    }

@router.post("/ask")
async def ask_question(question: str):
    return {
        "question":question,
        "answer":"Not implemented yet"
    }