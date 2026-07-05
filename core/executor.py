from core.registry import ToolRegistry


class ToolExecutor:

    def __init__(self, registry: ToolRegistry):

        self.registry = registry

    def execute(self, tool_name: str, arguments: dict):

        tool = self.registry.get(tool_name)

        if tool is None:

            raise Exception(f"Tool '{tool_name}' not found.")

        return tool.function(**arguments)