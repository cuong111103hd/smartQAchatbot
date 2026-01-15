import re

import re


def clean_text(text: str) -> str:
    """
    Clean raw PDF text WITHOUT breaking section structure
    """

    # Fix broken words (hyphen at line break)
    text = re.sub(r"-\n", "", text)

    # Replace newline inside sentence with space
    text = re.sub(r"\n(?=[a-z])", " ", text)

    # Remove excessive newlines
    text = re.sub(r"\n{2,}", "\n", text)

    # Normalize spaces
    text = re.sub(r"\s{2,}", " ", text)

    return text.strip()
