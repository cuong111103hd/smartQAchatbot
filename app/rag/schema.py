from typing import Optional, Dict

def build_metadata(
        paper_title: str,
        section: str,
        subsection: Optional[str],
        page: int
)-> Dict:
    return {
        "paper": paper_title,
        "section": section,
        "subsection": subsection,
        "page":page
    }