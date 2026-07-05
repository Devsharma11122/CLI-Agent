import json

from config import client, MODEL
from core.executor import ToolExecutor
from core.registry import ToolRegistry


class Agent:

    def __init__(
        self,
        registry: ToolRegistry,
        executor: ToolExecutor
    ):

        self.registry = registry
        self.executor = executor

        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful AI Coding Agent.\n"
                    "Whenever a tool is useful, use it.\n"
                    "Never pretend to create files.\n"
                    "Always use available tools."
                )
            }
        ]

    def run(self):

        while True:

            user_input = input("\nYou > ")

            if user_input.lower() == "exit":
                break

            self.messages.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )

            while True:

                response = client.chat.completions.create(

                    model=MODEL,

                    messages=self.messages,

                    tools=self.registry.get_openai_tools()
                )

                assistant = response.choices[0].message

                self.messages.append(assistant)

                if assistant.tool_calls:

                    for tool_call in assistant.tool_calls:

                        tool_name = tool_call.function.name

                        arguments = json.loads(
                            tool_call.function.arguments
                        )

                        print(
                            f"\n🔧 Tool: {tool_name}"
                        )

                        print(arguments)

                        result = self.executor.execute(
                            tool_name,
                            arguments
                        )

                        self.messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "content": result.model_dump_json()
                            }
                        )

                    continue

                print("\nAssistant:\n")

                print(assistant.content)

                break