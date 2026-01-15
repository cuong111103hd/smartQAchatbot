import re
from typing import List, Dict, Optional

def parse_sections(pages: List[Dict], paper_title: str) -> List[Dict]:
    """
    Parse pages of PDF text and attach section/subsection info.
    Multi-line safe: số và title có thể nằm trên nhiều dòng.
    Returns list of blocks:
    {
        "text": str,
        "page": int,
        "section": Optional[str],
        "subsection": Optional[str],
        "paper": str
    }
    """

    parsed_blocks = []

    current_section = None
    current_subsection = None

    pending_section_number = None
    pending_subsection_number = None

    # Regex patterns
    section_num_pattern = re.compile(r"^\s*(\d+)\s*$")          # e.g., "2"
    subsection_num_pattern = re.compile(r"^\s*(\d+\.\d+)\s*$") # e.g., "3.1"

    for page in pages:
        lines = page["text"].split("\n")

        for line in lines[:-1]:
            line = line.strip()
            if not line:
                continue

            # --- Section check ---
            sec_match = section_num_pattern.match(line)
            if sec_match:
                pending_section_number = sec_match.group(1)
                continue  # next line should be title

            # --- Subsection check ---
            sub_match = subsection_num_pattern.match(line)
            if sub_match:
                pending_subsection_number = sub_match.group(1)
                continue  # next line should be subsection title

            # --- Pending section number? ---
            if pending_section_number:
                current_section = line
                current_subsection = None  # reset subsection when new section
                pending_section_number = None
                # Don't continue: this line is section title, may contain content
                # fall through to parsed_blocks

            # --- Pending subsection number? ---
            elif pending_subsection_number:
                current_subsection = line
                pending_subsection_number = None
                # fall through

            # --- Append block ---
            parsed_blocks.append({
                "text": line,
                "page": page["page"],
                "section": current_section,
                "subsection": current_subsection,
                "paper": paper_title
            })

    return parsed_blocks
