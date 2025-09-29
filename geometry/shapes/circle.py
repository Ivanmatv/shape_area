import math

from .base import Shape
from ..exceptions import InvalidShapeError


class Circle(Shape):
    """A circle shape defined by its radius."""
    def __init__(self, radius: float):
        if radius <= 0:
            raise InvalidShapeError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle"""
        return math.pi * self.radius ** 2

    def is_right_angled(self) -> bool:
        """Circles are never right-angled"""
        return False

    def __repr__(self):
        return f"Circle(radius={self.radius})"