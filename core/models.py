from dataclasses import dataclass
from typing import Callable, Type

from pydantic import BaseModel


@dataclass
class Tool:

    name: str

    description: str

    input_model: Type[BaseModel]

    function: Callable


class ToolResult(BaseModel):

    success: bool

    message: str

    data: dict | None = None