from dataclasses import dataclass
from typing import Callable, Type

from pydantic import BaseModel


@dataclass
class Tool:

    """
    Represents one Tool inside our framework.
    """

    name: str

    description: str

    input_model: Type[BaseModel]

    function: Callable