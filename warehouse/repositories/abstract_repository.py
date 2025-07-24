from abc import ABC, abstractmethod
from domain.models import Item

class AbstractItemRepository(ABC):
    def __init__(self, filepath: str):
        self.filepath = filepath

    @abstractmethod
    def load_all(self) -> list[Item]:
        """
        Load all items from the storage.
        Returns a list of Item instances.
        """
        pass

    @abstractmethod
    def save_all(self, items: list[Item]) -> None:
        """
        Save all items to the storage.
        """
        pass
