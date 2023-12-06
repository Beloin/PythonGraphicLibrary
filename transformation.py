import math_utils
from types_3d import *
import math

from wireframe import Vec3DList


def rotate(point: Point3D, rotate_p: Point3D) -> Point3D:
    x_a = rotate_p[0]
    y_a = rotate_p[1]
    z_a = rotate_p[2]
    if x_a:
        angle = math.radians(x_a)
        sin = math.sin(angle)
        cos = math.cos(angle)
        point = (point[0],
                 point[1] * cos - point[2] * sin,
                 point[1] * sin + point[2] * cos)

    if y_a:
        angle = math.radians(y_a)
        sin = math.sin(angle)
        cos = math.cos(angle)
        point = (point[2] * sin + point[0] * cos,
                 point[1],
                 point[1] * cos - point[0] * sin)

    if z_a:
        angle = math.radians(z_a)
        sin = math.sin(angle)
        cos = math.cos(angle)
        point = (point[0] * cos - point[1] * sin,
                 point[0] * sin + point[1] * cos,
                 point[2])

    return point


def translate(point: Point3D, t: Point3D) -> Point3D:
    return point[0] + t[0], point[1] + t[1], point[2] + t[2]


def scale(point: Point3D, scale: Point3D) -> Point3D:
    return point[0] * scale[0], point[1] * scale[1], point[2] * scale[2]


def translate_edges(edges: Vec3DList, t: Point3D):
    new_edges = Vec3DList(sep=edges.sep())
    for vec3d in edges:
        p1 = translate(vec3d[0], t)
        p2 = translate(vec3d[1], t)
        new_edges.append((p1, p2))

    return new_edges


def rotate_edges(edges: Vec3DList, rotate_p: Point3D):
    new_edges = Vec3DList(sep=edges.sep())
    for vec3d in edges:
        p1 = rotate(vec3d[0], rotate_p)
        p2 = rotate(vec3d[1], rotate_p)
        new_edges.append((p1, p2))

    return new_edges


def scale_edges(edges: Vec3DList, scale_p: Point3D):
    new_edges = Vec3DList(sep=edges.sep())
    for vec3d in edges:
        p1 = scale(vec3d[0], scale_p)
        p2 = scale(vec3d[1], scale_p)
        new_edges.append((p1, p2))

    return new_edges


def scale_interval(edges: Vec3DList, new_scale: Scale, old_scale=(0, 1)):
    new_edges = Vec3DList(sep=edges.sep())
    for vec3d in edges:
        v1 = vec3d[0]
        v2 = vec3d[1]
        newv1 = tuple(map(lambda x: math_utils.scale_interval(x, old_scale, new_scale), v1))
        newv2 = tuple(map(lambda x: math_utils.scale_interval(x, old_scale, new_scale), v2))

        new_edges.append((newv1, newv2))  # type: ignore

    return new_edges


def scale_interval_arr(edges: list[Vector2D], new_scale: Scale, old_scale=(0, 1)):
    new_edges = []
    for vec2d in edges:
        v1 = vec2d[0]
        v2 = vec2d[1]
        newv1 = tuple(map(lambda x: math_utils.scale_interval(x, old_scale, new_scale), v1))
        newv2 = tuple(map(lambda x: math_utils.scale_interval(x, old_scale, new_scale), v2))

        new_edges.append((newv1, newv2))  # type: ignore

    return new_edges
