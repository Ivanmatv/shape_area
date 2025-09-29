import math

from .base import Shape
from ..exceptions import InvalidShapeError


class Triangle(Shape):
    """A triangle shape defined by three sides."""
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self._validate_sides(side_a, side_b, side_c)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def _validate_sides(self, a: float, b: float, c: float):
        """Validate triangle sides using triangle inequality theorem"""
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise InvalidShapeError("All sides must be positive")

        if not (a + b > c and a + c > b and b + c > a):
            raise InvalidShapeError("Invalid triangle sides")

    def area(self) -> float:
        """Calculate area using Heron's formula"""
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def is_right_angled(self, tolerance: float = 1e-7) -> bool:
        """Check if triangle is right-angled using Pythagorean theorem"""
        sides = sorted([self.side_a, self.side_b, self.side_c])
        return abs(sides[2]**2 - (sides[0]**2 + sides[1]**2)) <= tolerance

    def __repr__(self):
        return f"Triangle({self.side_a}, {self.side_b}, {self.side_c})"