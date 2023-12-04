# Based o n a -20:20 World
from types_3d import Point3D, Coord3D
import math_utils


def get_camera(at: Point3D, eye: Point3D) -> Coord3D:
    at_eye = (at[0] - eye[0], at[1] - eye[1], at[2] - eye[2])
    n = math_utils.normalize(at_eye)
    aux = (n[0], n[1], 0)  # TODO: Use random aux?
    aux_p = math_utils.project(aux, n)
    u = math_utils.minus(aux, aux_p)
    u = math_utils.normalize(u)
    v = math_utils.vetorial_product(u, n)

    return v, u, n


def point_to_camera(p: Point3D, camera: Coord3D, eye: Point3D) -> Point3D:
    # p' = RT * p
    #  | V1 V2 V3 0 |       | 1  0  0 E1 |
    #  | U1 U2 U3 0 |   *   | 0  1  0 E2 |
    #  | N1 N2 N3 0 |       | 0  0  1 E3 |
    #  | 0  0  0  1 |       | 0  0  0  1 |
    a1 = -eye[0] * camera[0][0] - eye[1] * camera[0][1] - eye[2] * camera[0][2]
    a2 = -eye[0] * camera[1][0] - eye[1] * camera[1][1] - eye[2] * camera[1][2]
    a3 = -eye[0] * camera[1][0] - eye[1] * camera[2][1] - eye[2] * camera[2][2]
    px = camera[0][0] * p[0] + camera[0][1] * p[1] + camera[0][2] * p[2] + a1
    py = camera[1][0] * p[0] + camera[1][1] * p[1] + camera[1][2] * p[2] + a2
    pz = camera[2][0] * p[0] + camera[2][1] * p[1] + camera[2][2] * p[2] + a3

    return px, py, pz

# TODO: Work with Perspective Porjection
