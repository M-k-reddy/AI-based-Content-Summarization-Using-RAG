import requests

class LLMGenerator:
    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "phi3:mini"

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)
        response.raise_for_status()

        return response.json()["response"].strip()
