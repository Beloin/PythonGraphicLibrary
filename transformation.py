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


def rotate(point: Point3D, x_a=None, y_a=None, z_a=None):
    res_pt = point

    # TODO: Implement multiplication
    if x_a:
        res_pt * get_rotation_mx_dpX(x_a)

    if y_a:
        res_pt * get_rotation_mx_dpX(y_a)

    if z_a:
        res_pt * get_rotation_mx_dpX(z_a)
