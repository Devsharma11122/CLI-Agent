import subprocess

from pydantic import BaseModel, Field

from core.base_tool import BaseTool
from core.models import Tool, ToolResult


class RunCommandInput(BaseModel):

    command: str = Field(
        ...,
        description="Shell command to execute."
    )


class RunCommandTool(BaseTool):

    def get_definition(self):

        return Tool(
            name="run_command",
            description="Runs a terminal command.",
            input_model=RunCommandInput,
            function=self.execute
        )

    def execute(self, command: str):

        try:

            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )

            return ToolResult(
                success=result.returncode == 0,
                message="Command executed.",
                data={
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "returncode": result.returncode
                }
            )

        except Exception as ex:

            return ToolResult(
                success=False,
                message=str(ex)
            )