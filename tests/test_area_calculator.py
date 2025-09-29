import math
import pytest

from geometry.calculators.area_calculator import calculate_area
from geometry.shapes import Circle, Triangle


class TestAreaCalculator:
    def test_circle_area(self):
        circle = Circle(2)
        assert calculate_area(circle) == 4 * math.pi

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        assert calculate_area(triangle) == 6.0

    def test_invalid_type(self):
        with pytest.raises(TypeError):
            calculate_area("not a shape")