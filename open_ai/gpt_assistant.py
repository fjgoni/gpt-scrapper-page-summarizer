# gpt_agent.py

from open_ai.openai_client import OpenAIClient


class GPTAgent:
    def __init__(self, client: OpenAIClient, system_prompt: str, model: str = "gpt-4o-mini"):
        self.client = client
        self.system_prompt = system_prompt
        self.model = model

    def run(self, user_input: str) -> str:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_input}
        ]
        return self.client.chat(model=self.model, messages=messages)
