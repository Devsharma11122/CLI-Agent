from registry import ToolRegistry
from tools.filesystem import CreateFolderTool
from agent import Agent


registry = ToolRegistry()

registry.register(
    CreateFolderTool()
)

agent = Agent(registry)

while True:

    query = input("\nYou > ")

    agent.chat(query)