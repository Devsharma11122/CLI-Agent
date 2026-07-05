from agent import Agent

from core.executor import ToolExecutor
from core.registry import ToolRegistry

from tools.filesystem import (
    CreateFolderTool,
    CreateFileTool,
    WriteFileTool,
    ReadFileTool
)


registry = ToolRegistry()

registry.register(CreateFolderTool())
registry.register(CreateFileTool())
registry.register(WriteFileTool())
registry.register(ReadFileTool())

executor = ToolExecutor(registry)

agent = Agent(
    registry,
    executor
)

agent.run()