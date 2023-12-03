from types_3d import *
import math


def get_rotation_mx_dpZ(angle):
    rad = math.radians(angle)
    x3_d = [
        [math.cos(rad), -math.sin(rad), 0],
        [math.sin(rad), math.cos(rad), 0],
        [0, 0, 1]
    ]

    return x3_d


def get_rotation_mx_dpY(angle):
    rad = math.radians(angle)
    x2_d = [
        [math.cos(rad), 0, math.sin(rad)],
        [0, 1, 0],
        [-math.sin(rad), 0, math.cos(rad)],
    ]

    return x2_d


def get_rotation_mx_dpX(angle):
    rad = math.radians(angle)
    x1_d = [
        [1, 0, 0],
        [0, math.cos(rad), math.sin(rad)],
        [0, -math.sin(rad), math.cos(rad)],
    ]

    return x1_d


def rotate(point: Point3D, x_a=None, y_a=None, z_a=None) -> Point3D:
    if x_a:
        angle = math.radians(x_a)
        sin = math.sin(angle)
        cos = math.cos(angle)
        return (point[0],
                point[1] * cos - point[2] * sin,
                point[1] * sin + point[2] * cos)

    if y_a:
        angle = math.radians(y_a)
        sin = math.sin(angle)
        cos = math.cos(angle)
        return (point[2] * sin + point[0] * cos,
                point[1],
                point[1] * cos - point[0] * sin)

    if z_a:
        angle = math.radians(z_a)
        sin = math.sin(angle)
        cos = math.cos(angle)
        return (point[0] * cos - point[1] * sin,
                point[0] * sin + point[1] * cos,
                point[2])


def translate(point: Point3D, t: Point3D) -> Point3D:
    return point[0] + t[0], point[1] + t[1], point[2] + t[2]


def scale(point: Point3D, scale: Point3D) -> Point3D:
    return point[0] * scale[0], point[1] * scale[1], point[2] * scale[2]
