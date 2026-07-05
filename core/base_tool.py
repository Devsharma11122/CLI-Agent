from abc import ABC, abstractmethod

from core.models import Tool


class BaseTool(ABC):

    @abstractmethod
    def get_definition(self) -> Tool:
        """
        Returns tool metadata.
        """
        pass

    @abstractmethod
    def execute(self, **kwargs):
        """
        Executes the tool.
        """
        pass