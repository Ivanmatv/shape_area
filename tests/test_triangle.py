import pytest

from geometry.shapes import Triangle
from geometry.exceptions import InvalidShapeError


class TestTriangle:
    def test_area(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.area() == 6.0

    def test_right_angled(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.is_right_angled()

    def test_not_right_angled(self):
        triangle = Triangle(3, 4, 6)
        assert not triangle.is_right_angled()

    def test_invalid_triangle(self):
        with pytest.raises(InvalidShapeError):
            Triangle(1, 1, 3)

    def test_negative_sides(self):
        with pytest.raises(InvalidShapeError):
            Triangle(-1, 2, 2)