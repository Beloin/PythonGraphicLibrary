from types_3d import Point3D, Size, Z, Point2D, X, Y, Vector2D
from wireframe import Vec3DList


def perspective(p: Point3D, eye: Point3D, window: Size) -> Point2D:
    d = eye[Z]
    dz = p[Z] / d
    xnew = p[X] * dz
    ynew = p[Y] * dz
    return xnew, ynew


def perspective_edges(edges: Vec3DList, eye: Point3D, window: Size) -> list[Vector2D]:
    vec: list[Vector2D] = []
    for i in edges:
        x_1, y_1 = perspective(i[0], eye, window)
        x_2, y_2 = perspective(i[1], eye, window)

        s: Point2D = (x_1, y_1)
        e: Point2D = (x_2, y_2)
        vec.append((s, e))

    return vec
