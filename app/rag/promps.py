SYSTEM_PROMPT = """You are an expert machine learning researcher. YOu must answer strictly based on the provided context from the paper. If the answer is not in the context, say you do not know. Use preceise technical language.
"""

USER_PROMPT_TEMPLATE = """
Question: 
{question}

Context: 
{context}

Instruction: 
- Answer step by step
- Explain key concepts clearly
- Cite the section and page numbers in your answer
"""



