from pathlib import Path

from pydantic import BaseModel, Field

from core.base_tool import BaseTool
from core.models import Tool, ToolResult


WORKSPACE = Path("workspace")


class CreateFolderInput(BaseModel):
    path: str = Field(
        ...,
        description="Folder name or relative path to create inside workspace."
    )


class CreateFolderTool(BaseTool):

    def get_definition(self) -> Tool:

        return Tool(
            name="create_folder",
            description="Creates a folder inside the workspace.",
            input_model=CreateFolderInput,
            function=self.execute
        )

    def execute(self, path: str):

        folder = WORKSPACE / path

        try:

            folder.mkdir(parents=True, exist_ok=True)

            return ToolResult(
                success=True,
                message=f"Folder '{path}' created successfully.",
                data={
                    "path": str(folder)
                }
            )

        except Exception as ex:

            return ToolResult(
                success=False,
                message=str(ex)
            )