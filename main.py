from registry import ToolRegistry

from tools.filesystem import CreateFolderTool

registry = ToolRegistry()

registry.register(
    CreateFolderTool()
)

tool = registry.get(
    "create_folder"
)

result = tool.execute(
    path="TodoApp"
)

print(result)