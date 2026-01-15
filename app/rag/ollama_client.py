import subprocess

class OllamaClientCLI:
    def __init__(self, model: str = "qwen2.5:7b"):
        self.model = model

    def chat(self, system: str, user: str) -> str:
        prompt = f"{system}\n{user}"
        result = subprocess.run(
            ["ollama", "run", self.model],
            input=prompt.encode("utf-8"),
            capture_output=True
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr.decode("utf-8"))

        return result.stdout.decode("utf-8").strip()
