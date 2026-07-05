from dataclasses import dataclass
from typing import Callable, Type

from pydantic import BaseModel


@dataclass
class Tool:
    """
    Metadata about a tool.
    """

    name: str

    description: str

    input_model: Type[BaseModel]

    function: Callable


@dataclass
class ToolResult:
    """
    Standard response returned by every tool.
    """

    success: bool

    message: str

    data: dict | None = None