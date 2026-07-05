from pathlib import Path

from pydantic import BaseModel, Field

from core.base_tool import BaseTool
from core.models import Tool, ToolResult


WORKSPACE = Path("workspace")


# ==========================================================
# CREATE FOLDER
# ==========================================================

class CreateFolderInput(BaseModel):
    path: str = Field(
        ...,
        description="Folder path inside workspace."
    )


class CreateFolderTool(BaseTool):

    def get_definition(self):

        return Tool(
            name="create_folder",
            description="Creates a folder inside workspace.",
            input_model=CreateFolderInput,
            function=self.execute
        )

    def execute(self, path: str):

        try:

            folder = WORKSPACE / path

            folder.mkdir(parents=True, exist_ok=True)

            return ToolResult(
                success=True,
                message=f"Folder '{path}' created.",
                data={
                    "path": str(folder)
                }
            )

        except Exception as ex:

            return ToolResult(
                success=False,
                message=str(ex)
            )


# ==========================================================
# CREATE FILE
# ==========================================================

class CreateFileInput(BaseModel):

    path: str = Field(
        ...,
        description="Relative file path inside workspace."
    )


class CreateFileTool(BaseTool):

    def get_definition(self):

        return Tool(
            name="create_file",
            description="Creates an empty file.",
            input_model=CreateFileInput,
            function=self.execute
        )

    def execute(self, path: str):

        try:

            file = WORKSPACE / path

            file.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            file.touch(exist_ok=True)

            return ToolResult(
                success=True,
                message=f"File '{path}' created.",
                data={
                    "path": str(file)
                }
            )

        except Exception as ex:

            return ToolResult(
                success=False,
                message=str(ex)
            )


# ==========================================================
# WRITE FILE
# ==========================================================

class WriteFileInput(BaseModel):

    path: str

    content: str


class WriteFileTool(BaseTool):

    def get_definition(self):

        return Tool(
            name="write_file",
            description="Writes content into a file.",
            input_model=WriteFileInput,
            function=self.execute
        )

    def execute(self, path: str, content: str):

        try:

            file = WORKSPACE / path

            file.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            file.write_text(
                content,
                encoding="utf-8"
            )

            return ToolResult(
                success=True,
                message=f"Content written to '{path}'.",
                data={
                    "path": str(file)
                }
            )

        except Exception as ex:

            return ToolResult(
                success=False,
                message=str(ex)
            )


# ==========================================================
# READ FILE
# ==========================================================

class ReadFileInput(BaseModel):

    path: str


class ReadFileTool(BaseTool):

    def get_definition(self):

        return Tool(
            name="read_file",
            description="Reads a file.",
            input_model=ReadFileInput,
            function=self.execute
        )

    def execute(self, path: str):

        try:

            file = WORKSPACE / path

            if not file.exists():

                return ToolResult(
                    success=False,
                    message="File does not exist."
                )

            content = file.read_text(
                encoding="utf-8"
            )

            return ToolResult(
                success=True,
                message="File read successfully.",
                data={
                    "content": content
                }
            )

        except Exception as ex:

            return ToolResult(
                success=False,
                message=str(ex)
            )
        

class ListDirectoryInput(BaseModel):

    path: str = Field(
        default="",
        description="Directory inside workspace to inspect."
    )

class ListDirectoryTool(BaseTool):

    def get_definition(self):

        return Tool(
            name="list_directory",
            description="Lists all files and folders inside a directory.",
            input_model=ListDirectoryInput,
            function=self.execute
        )

    def execute(self, path: str = ""):

        try:

            directory = WORKSPACE / path

            if not directory.exists():

                return ToolResult(
                    success=False,
                    message="Directory does not exist."
                )

            if not directory.is_dir():

                return ToolResult(
                    success=False,
                    message="Path is not a directory."
                )

            items = []

            for item in directory.iterdir():

                items.append(
                    {
                        "name": item.name,
                        "type": "folder" if item.is_dir() else "file"
                    }
                )

            return ToolResult(
                success=True,
                message="Directory listed successfully.",
                data={
                    "items": items
                }
            )

        except Exception as ex:

            return ToolResult(
                success=False,
                message=str(ex)
            )