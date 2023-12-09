import copy
import math
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
    _sep: int
    _center: Point3D
    _color: str

    def __init__(self, data=None, sep=None, center=None, color=None):
        self._data = [] if data is None else data
        self._center = [] if center is None else center
        self._color = [] if color is None else color
        if sep is not None:
            self._sep = sep

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

    def sep(self):
        return self._sep

    def center(self, new_center=None):
        if new_center:
            self._center = new_center

        return self._center

    def color(self):
        return self._color


# TODO: Maybe use -1 to 1? Problem with size while using edge and origin
# TODO: Create a version where we convert from Object to World.. SO since that, we won't be needding -1 to 1?
# TODO: Everything here is wrong, we need to have edges from the small blocks, not full with big blocks... Do we change it?
def cube(edge: float, res=.5, dist=0) -> Vec3DList:  # TODO: Use origin as 0...
    """
    Define a cube in its own object coordinates: based on 0.0 to 1.0
    @param edge size of the edge in number between 0 and 1
    @param res resolution used to calculate inbetween the cube small cubes, usually from 0 to 1.
    @param dist Param to "Simulate" 3D Cube into a 2D rep.
    """
    assert 0 < edge <= 1.0, "Edge must be between 1 and 0"
    vector = Vec3DList(sep=4)
    origin = 1 - edge

    last_p1 = None
    last_p2 = None
    last_p3 = None
    last_p4 = None

    # Z Stepper
    step = 1 if res == 0 else (1 / (res * 10))
    end = 0
    while end <= 1:
        # Simulate 3D into 2D for debug purposes
        virtual = dist * end

        curr_z_pos = origin + (edge * end)
        m_p1 = (origin + virtual, origin + virtual, curr_z_pos)
        m_p2 = (origin + edge + virtual, origin + virtual, curr_z_pos)

        m_p4 = (origin + virtual, origin + edge + virtual, curr_z_pos)
        m_p3 = (origin + edge + virtual, origin + edge + virtual, curr_z_pos)

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
    step = 1 if res == 0 else (1 / (res * 10))
    end = 0
    while end <= 1:
        # Simulate 3D into 2D for debug purposes
        virtual = dist * end

        curr_y_pos = origin + (edge * end)
        m_p1 = (origin + virtual, curr_y_pos, origin)
        m_p2 = (origin + edge + virtual, curr_y_pos, origin)

        m_p3 = (origin + edge + virtual, curr_y_pos, origin + edge)
        m_p4 = (origin + virtual, curr_y_pos, origin + edge)

        vector.append((m_p1, m_p2))
        vector.append((m_p2, m_p3))
        vector.append((m_p3, m_p4))
        vector.append((m_p4, m_p1))

        end += step

    # X Stepper
    step = 1 if res == 0 else (1 / (res * 10))
    end = 0
    while end <= 1:
        # Simulate 3D into 2D for debug purposes
        virtual = dist * end

        curr_x_pos = origin + (edge * end)
        m_p1 = (curr_x_pos, origin + virtual, origin)
        m_p2 = (curr_x_pos, origin + edge + virtual, origin)

        m_p3 = (curr_x_pos, origin + edge + virtual, origin + edge)
        m_p4 = (curr_x_pos, origin + virtual, origin + edge)

        vector.append((m_p1, m_p2))
        vector.append((m_p2, m_p3))
        vector.append((m_p3, m_p4))
        vector.append((m_p4, m_p1))

        end += step

    return vector


def sphere(radius: float, res=.5, circle_res=.5) -> Vec3DList:
    # C = 2*pi*R
    # sen(x) = CO/H
    # H = R

    # 1. Generate small circle
    # 2. Generate points
    # 3. Append-it to vector list
    assert 0 < radius <= 1.0, "radius must be between 1 and 0"

    origin = 1 - radius
    amount = circle_res * 100
    angle_step = 360 / amount

    vector = Vec3DList(sep=amount)

    # Z Stepper
    step = 1 if res == 0 else (1 / (res * 100))
    end = 0
    while end < 1:
        circle_pt = __get_circle_point(radius, 360 * end)

        cur_z = origin + circle_pt[1]
        n_radius = circle_pt[0]

        last_pt = None
        cur_angle = 0
        while cur_angle <= 360:
            x, y = __get_circle_point(n_radius, cur_angle)
            x += origin
            y += origin

            if last_pt is not None:
                vector.append((last_pt, (x, y, cur_z)))

            last_pt = (x, y, cur_z)
            cur_angle += angle_step

        last_pt = None
        cur_angle = 0
        while cur_angle <= 360:
            x, y = __get_circle_point(n_radius, cur_angle)
            x += origin
            y += origin

            if last_pt is not None:
                vector.append((last_pt, (cur_z, x, y)))

            last_pt = (cur_z, x, y)
            cur_angle += angle_step

        end += step

    return vector


def __get_circle_point(radius, angle):
    """
    Gets circle point based on circle origin with value 0
    """
    # sen(x) = CO/H
    # cos(x) = CA/H
    sin = math.sin(math.radians(angle))
    cos = math.cos(math.radians(angle))
    y = radius * sin
    x = radius * cos
    return x, y


def cone(radius: float, res=.5, circle_res=.5):
    assert 0 < radius <= 1.0, "radius must be between 1 and 0"

    origin = 1 - radius
    amount = circle_res * 100
    angle_step = 360 / amount

    vector = Vec3DList(sep=amount)

    # First circle
    last_pt = None
    cur_angle = 0
    while cur_angle <= 360:
        x, y = __get_circle_point(radius, cur_angle)
        x += origin
        y += origin

        if last_pt is not None:
            vector.append((last_pt, (x, y, origin)))

        last_pt = (x, y, origin)
        cur_angle += angle_step

    # TODO: Create a triangle and rotate it to make the cone
