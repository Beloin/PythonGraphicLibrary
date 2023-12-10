import math

from types_3d import Point3D, Size, Z, Point2D, X, Y, Vector2D, Scale
from wireframe import Vec3DList


def weak_perspective(p: Point3D, eye: Point3D, window: Size) -> Point2D:
    d = eye[Z]
    dz = p[Z] / d
    xnew = p[X] * dz
    ynew = p[Y] * dz
    return xnew, ynew


def weak_perspective_edges(edges: Vec3DList, eye: Point3D, window: Size) -> list[Vector2D]:
    vec: list[Vector2D] = []
    for i in edges:
        x_1, y_1 = weak_perspective(i[0], eye, window)
        x_2, y_2 = weak_perspective(i[1], eye, window)

        s: Point2D = (x_1, y_1)
        e: Point2D = (x_2, y_2)
        vec.append((s, e))

    return vec


def strong_projection(p: Point3D, eye: Point3D, display_pos: Point3D, size: Scale) -> Point2D:
    # | 2*near / right-left          0              right+left/right-left                  0          |
    # |        0             2*near / top-bottom    top+bottom/top-bottom                  0          |
    # |        0                     0               -(far+near/far-near)         -2far*near/far-near |
    # |        0                     0
    bx = 0
    by = 0

    return bx, by


def strong_proj(up, close):
    angle = math.atan(up / close)


def strongperspective_edges(edges: Vec3DList, eye: Point3D, display: Point3D, window: Size) -> list[Vector2D]:
    vec: list[Vector2D] = []
    for i in edges:
        x_1, y_1 = strong_projection(i[0], eye, display, window)
        x_2, y_2 = strong_projection(i[1], eye, display, window)

        s: Point2D = (x_1, y_1)
        e: Point2D = (x_2, y_2)
        vec.append((s, e))

    return vec
