from core.executor import ToolExecutor
from core.registry import ToolRegistry

from tools.filesystem import CreateFolderTool


registry = ToolRegistry()

registry.register(CreateFolderTool())

executor = ToolExecutor(registry)

result = executor.execute(
    "create_folder",
    {
        "path": "TodoApp"
    }
)

print(result)