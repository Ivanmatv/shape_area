from geometry.shapes.base import Shape


def calculate_area(shape: Shape) -> float:
    """Calculate area of any shape without knowing its type at compile-time."""

    if not isinstance(shape, Shape):
        raise TypeError("shape must be an instance of Shape")

    return shape.area()