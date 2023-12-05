# Based o n a -20:20 World
import random

from types_3d import Point3D, Coord3D
import math_utils
from wireframe import Vec3DList
import numpy as np


def get_camera(at: Point3D, eye: Point3D) -> Coord3D:
    assert at != eye, "`at` should be different than `eye`"
    at_eye = (at[0] - eye[0], at[1] - eye[1], at[2] - eye[2])
    n = math_utils.normalize(at_eye)
    aux = (n[0], random.randint(0, 100) / 100, n[2])
    if aux[0] == 0 and aux[2] == 0:
        aux = (aux[0], aux[1], random.randint(0, 100) / 100)

    aux_p = math_utils.project(aux, n)
    u = math_utils.minus(aux, aux_p)
    u = math_utils.normalize(u)
    v = math_utils.vetorial_product(u, n)

    return u, v, n  # TODO: Check which is better...


def point_to_camera(p: Point3D, camera: Coord3D, eye: Point3D) -> Point3D:
    # p' = RT * p
    #  | V1 V2 V3 0 |       | 1  0  0 E1 |
    #  | U1 U2 U3 0 |   *   | 0  1  0 E2 |
    #  | N1 N2 N3 0 |       | 0  0  1 E3 |
    #  | 0  0  0  1 |       | 0  0  0  1 |
    a1 = -eye[0] * camera[0][0] - eye[1] * camera[0][1] - eye[2] * camera[0][2]
    a2 = -eye[0] * camera[1][0] - eye[1] * camera[1][1] - eye[2] * camera[1][2]
    a3 = -eye[0] * camera[2][0] - eye[1] * camera[2][1] - eye[2] * camera[2][2]
    px = camera[0][0] * p[0] + camera[0][1] * p[1] + camera[0][2] * p[2] + a1
    py = camera[1][0] * p[0] + camera[1][1] * p[1] + camera[1][2] * p[2] + a2
    pz = camera[2][0] * p[0] + camera[2][1] * p[1] + camera[2][2] * p[2] + a3

    return px, py, pz


def edges_to_camera(edges: Vec3DList, camera: Coord3D, eye: Point3D):
    new_edges = Vec3DList(sep=edges.sep())
    for edge in edges:
        p1 = point_to_camera(edge[0], camera, eye)
        p2 = point_to_camera(edge[1], camera, eye)
        new_edges.append((p1, p2))

    return new_edges


if __name__ == '__main__':
    at = (0, 0, 0)
    eye = (0, 0, 1)
    camera = get_camera(at, eye)
    print(camera)
