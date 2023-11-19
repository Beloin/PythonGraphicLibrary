Point3D = tuple[float, float, float]
"""
Based with X_1, X_2, X_3
"""

Vector3D = tuple[Point3D, Point3D]
Size = tuple[int, int]


class Vec3D:
    """
    List of 3D Vector items.

    Example:
        [
            ( (x1, y1, z1), (x1, y1, z1) ),
            ( (x1, y1, z1), (x1, y1, z1) ),
            ...
        ]
    """
    _data: list[Vector3D]

    def __init__(self, data=None):
        self._data = [] if data is None else data

    def __getitem__(self, item: int):
        return self._data[item]


def cube(edge: float, res=.5, origin=.5) -> Vec3D:
    """
    Define a cube in its own object coordinates: based on 0.0 to 1.0
    @param edge size of the edge
    @param res resolution used to calculate inbetween the cube small cubes.
    @param origin cube origin
    """
    vector = Vec3D()

    return vector
