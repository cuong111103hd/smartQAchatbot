from app.rag.promps import SYSTEM_PROMPT,USER_PROMPT_TEMPLATE

class RAGGenerator: 
    def __init__(self,llm_client):
        self.llm = llm_client

    def generate(self, question: str, context: str)-> str:
        prompt = USER_PROMPT_TEMPLATE.format(
            question = question,
            context = context
        )

        response = self.llm.chat(
            system = SYSTEM_PROMPT,
            user = prompt
        )

        return response