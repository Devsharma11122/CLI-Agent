from pathlib import Path

from pydantic import BaseModel

from config import WORKSPACE
from models import Tool
from tools.base import BaseTool


class CreateFolderInput(BaseModel):
    path: str


class CreateFolderTool(BaseTool):

    def get_definition(self):

        return Tool(

            name="create_folder",

            description="Creates a folder inside workspace.",

            input_model=CreateFolderInput,

            function=self.execute
        )

    def execute(self, path: str):

        folder = WORKSPACE / path

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return {

            "success": True,

            "folder": str(folder)

        }