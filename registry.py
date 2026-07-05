from models import Tool


class ToolRegistry:

    def __init__(self):
        self._tools = {}

    def register(self, tool):
        definition = tool.get_definition()
        self._tools[definition.name] = definition

    def get(self, name):
        return self._tools.get(name)

    def execute(self, name: str, **kwargs):

        tool = self.get(name)

        if tool is None:
            raise Exception(f"Tool '{name}' not found.")

        return tool.function(**kwargs)

    def get_openai_tools(self):

        openai_tools = []

        for tool in self._tools.values():

            openai_tools.append({
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.input_model.model_json_schema()
                }
            })

        return openai_tools