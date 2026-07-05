import json

from config import client, MODEL


class Agent:

    def __init__(self, registry):

        self.registry = registry

    def chat(self, user_message: str):

        messages = [
            {
                "role": "system",
                "content": (
                    "You are an AI Coding Assistant. "
                    "Use tools whenever needed."
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ]

        while True:

            response = client.chat.completions.create(

                model=MODEL,

                messages=messages,

                tools=self.registry.get_openai_tools()

            )

            assistant_message = response.choices[0].message

            messages.append(assistant_message)

            # ---------------------------------------------------
            # Did the model ask for a tool?
            # ---------------------------------------------------

            if assistant_message.tool_calls:

                for tool_call in assistant_message.tool_calls:

                    tool_name = tool_call.function.name

                    arguments = json.loads(
                        tool_call.function.arguments
                    )

                    print(f"\n🔧 Tool Selected : {tool_name}")
                    print(f"📥 Arguments     : {arguments}")

                    tool_result = self.registry.execute(
                        tool_name,
                        **arguments
                    )

                    print(f"📤 Tool Result   : {tool_result}")

                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": json.dumps(tool_result)
                        }
                    )

                continue

            # ---------------------------------------------------
            # No tool call
            # Final answer
            # ---------------------------------------------------

            print("\n🤖 Assistant\n")
            print(assistant_message.content)

            break