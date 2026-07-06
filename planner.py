from pydantic import BaseModel
from openai import OpenAI

from config import MODEL


class Plan(BaseModel):
    steps: list[str]


class Planner:

    def __init__(self, client: OpenAI):
        self.client = client

    def create_plan(self, user_request: str) -> list[str]:

        response = self.client.beta.chat.completions.parse(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": """
You are an expert software architect.

Your job is NOT to execute anything.

Break the user's request into small executable steps.

Return only the plan.
"""
                },
                {
                    "role": "user",
                    "content": user_request
                }
            ],
            response_format=Plan
        )

        return response.choices[0].message.parsed.steps