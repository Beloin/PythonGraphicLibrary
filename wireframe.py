import copy

from types_3d import *


class Vec3DList:
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

    def append(self, vec: Vector3D):
        self._data.append(vec)

    def raw(self):
        return copy.deepcopy(self._data)

    def __repr__(self):
        return self._data.__repr__()

    def __str__(self):
        return self._data.__str__()

    def __iter__(self):
        return self._data.__iter__()


# TODO: Maybe use -1 to 1?
# TODO: Create a version where we convert from Object to World.. SO since that, we won't be needding -1 to 1?
def cube(edge: float, res=.5, origin=.1, dist=0) -> Vec3DList:
    """
    Define a cube in its own object coordinates: based on 0.0 to 1.0
    @param edge size of the edge in number between 0 and 1
    @param res resolution used to calculate inbetween the cube small cubes, usually from 0 to 1.
    @param origin cube origin
    @param dist Param to "Simulate" 3D Cube into a 2D rep.
    """
    assert 0 < edge <= 1.0
    vector = Vec3DList()

    half_edge = edge / 2

    # "Fisrt" Square
    f_p1 = (origin - half_edge, origin - half_edge, origin)
    f_p2 = (origin + half_edge, origin - half_edge, origin)
    f_p4 = (f_p1[0], f_p1[1] + edge, origin)
    f_p3 = (f_p2[0], f_p2[1] + edge, origin)

    vector.append((f_p1, f_p2))
    vector.append((f_p2, f_p3))
    vector.append((f_p3, f_p4))
    vector.append((f_p4, f_p1))

    # # Simulate 3D into 2D
    origin += dist
    # step = 1 if res == 0 else (1 / (res * 100))
    # while step < 1:
    #     m_p1 = (origin - half_edge, origin - half_edge, origin - (half_edge * step))
    #     m_p2 = (origin + half_edge, origin - half_edge, origin - (half_edge * step))
    #     m_p4 = (m_p1[0], m_p1[1] + edge, m_p1[2])
    #     m_p3 = (m_p2[0], m_p2[1] + edge, m_p2[2])
    #
    #     vector.append((m_p1, m_p2))
    #     vector.append((m_p2, m_p3))
    #     vector.append((m_p3, m_p4))
    #     vector.append((m_p4, m_p1))

    # Last Square
    b_p1 = (origin - half_edge, origin - half_edge, origin - half_edge)
    b_p2 = (origin + half_edge, origin - half_edge, origin - half_edge)
    b_p4 = (b_p1[0], b_p1[1] + edge, b_p1[2])
    b_p3 = (b_p2[0], b_p2[1] + edge, b_p2[2])

    # Square connections
    vector.append((b_p1, b_p2))
    vector.append((b_p2, b_p3))
    vector.append((b_p3, b_p4))
    vector.append((b_p4, b_p1))

    vector.append((f_p1, b_p1))
    vector.append((f_p2, b_p2))
    vector.append((f_p3, b_p3))
    vector.append((f_p4, b_p4))

    return vector
