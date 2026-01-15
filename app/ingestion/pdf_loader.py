import fitz #PyMuPDF
from typing import List,Dict

def load_pdf(path: str) -> List[Dict]:
    """
    Load PDF and return list of pages with text and metadata
    """

    doc = fitz.open(path)
    pages = []

    for page_number, page in enumerate(doc, start = 1):
        text = page.get_text("text")

        pages.append({
            "page": page_number,
            "text": text
        })

    return pages