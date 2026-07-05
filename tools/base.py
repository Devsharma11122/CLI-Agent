from abc import ABC, abstractmethod

from models import Tool


class BaseTool(ABC):

    @abstractmethod
    def get_definition(self) -> Tool:
        """
        Returns metadata about the tool.
        """
        pass

    @abstractmethod
    def execute(self, **kwargs):
        """
        Executes the tool.
        """
        pass