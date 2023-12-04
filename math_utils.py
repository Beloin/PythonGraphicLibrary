import math

from types_3d import Point3D


def minus(a: Point3D, b: Point3D) -> Point3D:
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def project(p: Point3D, n: Point3D) -> Point3D:
    a = p[0] * n[0] + p[1] * n[1] + p[2] * n[2]
    b = n[0] * n[0] + n[1] * n[1] + n[2] * n[2]
    res = a / b
    return n[0] * res, n[1] * res, n[0] * res


def normalize(p: Point3D) -> Point3D:
    res = p[0] * p[0] + p[1] * p[1] + p[2] * p[2]
    res = math.sqrt(res)
    return p[0] / res, p[1] / res, p[0] / res


def vetorial_product(u: Point3D, n: Point3D) -> Point3D:
    i = u[1] * n[2] - u[2] * n[1]
    j = u[2] * n[0] - u[0] * n[2]
    k = u[0] * n[1] - u[1] * n[0]
    return i, j, k
