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

    def __len__(self):
        return self._data.__len__()


# TODO: Maybe use -1 to 1?
# TODO: Create a version where we convert from Object to World.. SO since that, we won't be needding -1 to 1?
def cube(edge: float, res=.5, origin=.5, dist=0) -> Vec3DList:
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

    last_p1 = None
    last_p2 = None
    last_p3 = None
    last_p4 = None

    # Z Stepper
    step = 1 if res == 0 else (1 / (res * 100))
    end = 0
    while end <= 1:
        # Simulate 3D into 2D for debug purposes
        virtual = dist * end

        curr_z_pos = origin - (half_edge * end)
        m_p1 = (origin - half_edge + virtual, origin - half_edge + virtual, curr_z_pos)
        m_p2 = (origin + half_edge + virtual, origin - half_edge + virtual, curr_z_pos)

        m_p4 = (origin - half_edge + virtual, origin + half_edge + virtual, curr_z_pos)
        m_p3 = (origin + half_edge + virtual, origin + half_edge + virtual, curr_z_pos)

        vector.append((m_p1, m_p2))
        vector.append((m_p2, m_p3))
        vector.append((m_p3, m_p4))
        vector.append((m_p4, m_p1))

        # Joints
        if last_p1 is not None:
            vector.append((last_p1, m_p1))
            vector.append((last_p2, m_p2))
            vector.append((last_p3, m_p3))
            vector.append((last_p4, m_p4))

        last_p1 = m_p1
        last_p2 = m_p2
        last_p3 = m_p3
        last_p4 = m_p4

        end += step

    # Y Stepper
    # step = 1 if res == 0 else (1 / (res * 100))
    # end = 0
    # while end <= 1:
    #     # Simulate 3D into 2D for debug purposes
    #     virtual = dist * end
    #
    #     curr_y_pos = origin + (half_edge * end)
    #     m_p1 = (origin - half_edge + virtual, curr_y_pos, origin + half_edge)
    #     m_p2 = (origin + half_edge + virtual, curr_y_pos, origin + half_edge)
    #
    #     m_p3 = (origin + half_edge + virtual, curr_y_pos, origin - half_edge)
    #     m_p4 = (origin - half_edge + virtual, curr_y_pos, origin - half_edge)
    #
    #     vector.append((m_p1, m_p2))
    #     vector.append((m_p2, m_p3))
    #     vector.append((m_p3, m_p4))
    #     vector.append((m_p4, m_p1))
    #
    #     # Joints
    #     # if last_p1 is not None:
    #     #     vector.append((last_p1, m_p1))
    #     #     vector.append((last_p2, m_p2))
    #     #     vector.append((last_p3, m_p3))
    #     #     vector.append((last_p4, m_p4))
    #     #
    #     # last_p1 = m_p1
    #     # last_p2 = m_p2
    #     # last_p3 = m_p3
    #     # last_p4 = m_p4
    #
    #     end += step

    return vector
