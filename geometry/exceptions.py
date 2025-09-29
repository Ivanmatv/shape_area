class GeometryError(Exception):
    """Base exception for geometry library"""
    pass


class InvalidShapeError(GeometryError):
    """Raised when shape parameters are invalid"""
    pass