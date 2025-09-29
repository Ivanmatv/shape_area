import pytest
import math

from geometry.shapes import Circle
from geometry.exceptions import InvalidShapeError


class TestCircle:
    def test_area(self):
        circle = Circle(5)
        expected_area = math.pi * 25
        assert circle.area() == expected_area

    def test_zero_radius(self):
        with pytest.raises(InvalidShapeError):
            Circle(0)

    def test_negative_radius(self):
        with pytest.raises(InvalidShapeError):
            Circle(-1)

    def test_is_right_angled(self):
        circle = Circle(5)
        assert not circle.is_right_angled()