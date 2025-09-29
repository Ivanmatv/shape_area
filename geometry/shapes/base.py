from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def is_right_angled(self) -> bool:
        pass

    def __str__(self) -> str:
        return self.__class__.__name__