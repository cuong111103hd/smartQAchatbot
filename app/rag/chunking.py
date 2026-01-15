from typing import List, Dict

MAX_CHUNK_SIZE = 800 

def semantic_chunking(blocks: List[Dict], paper_title: str)->List[Dict]:
    chunks = []
    current_text = ""
    current_meta = None

    for block in blocks:
        text = block["text"]

        if current_meta is None:
            current_meta = {
                "paper": paper_title,
                "section": block["section"],
                "subsection": block["subsection"],
                "page": block["page"]
            }

        if (
            block["section"] != current_meta["section"]
            or len(current_text) + len(text) > MAX_CHUNK_SIZE
        ):
            chunks.append({
                "text": current_text.strip(),
                "metadata": current_meta
            })
            current_text = ""
            current_meta = {
                "paper": paper_title,
                "section": block["section"],
                "subsection": block["subsection"],
                "page":block["page"]
            }
        
        current_text = " " + text

    if current_text: 
        chunks.append({
            "text": current_text.strip(),
            "metadata": current_meta
        })

    return chunks