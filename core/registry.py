from core.base_tool import BaseTool


class ToolRegistry:

    def __init__(self):

        self._tools = {}

    def register(self, tool: BaseTool):

        definition = tool.get_definition()

        self._tools[definition.name] = definition

    def get(self, name: str):

        return self._tools.get(name)

    def get_all(self):

        return list(self._tools.values())

    def get_openai_tools(self):

        tools = []

        for tool in self._tools.values():

            tools.append(
                {
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.input_model.model_json_schema()
                    }
                }
            )

        return tools