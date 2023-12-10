import threading
from time import sleep

import matplotlib.pyplot as plt
import matplotlib

import solids.solids as solids

import transformation
from types_3d import Point3D
from utils_3d import draw_coordinate_system, get_mean_point
from wireframe import Vec3DList

from camera_persp import camera

matplotlib.use('qtagg')

solid = solids.Solid()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
world2cam = False


def configure():
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)
    ax.set_aspect("equal")

    if not world2cam:
        draw_coordinate_system(ax, size=10)


def main(solid_list):
    # World is -10 to 10

    new_solid_list = []
    if world2cam:
        octante = 1
        for item in solid_list:
            if octante == get_octant_number(item.center()):
                new_solid_list.append(item)

        at = get_mean_point(new_solid_list)
        eye = (4, -4, 4)
        cam = camera.get_camera(at, eye)
    else:
        new_solid_list.extend(solid_list)
        at = (2, 7, 5)
        eye = (4, -4, 4)
        cam = camera.get_camera(at, eye)

    eye_rep = solid.sphere2(color="red")  # 0 -> 1
    at_rep = solid.sphere2(color="gray")  # 0 -> 1
    eye_rep = transformation.translate_edges(eye_rep, eye)
    at_rep = transformation.translate_edges(at_rep, at)

    # Scale solids to show in real world
    for item in new_solid_list:
        item.update(transformation.scale_solid(item, (2, 2, 2)))

    # If showing in camera, get new world position and new solids positions
    if world2cam:
        to_camera = camera.point_to_camera((0, 0, 0), cam, eye)
        world_pt = solid.sphere2(color="#db3265")  # 0 -> 1
        world_pt = transformation.translate_edges(world_pt, to_camera)

        for item in new_solid_list:
            item.update(camera.edges_to_camera(item, cam, eye))

    ax.clear()
    configure()

    # Eye coordinate System
    draw_coordinate_system(ax, eye, size=5, txt="eye")

    if not world2cam:
        draw_coordinate_system(ax, at, size=5, txt="at")

    for item in new_solid_list:
        if world2cam:
            # Draw New World transformation
            draw_coordinate_system(ax, to_camera, size=5, txt="World")
            plot_axis(world_pt)
            plot_axis(item)
        else:
            plot_axis(item)
            plot_axis(at_rep)

        plot_axis(eye_rep)

        fig.canvas.draw()
        fig.canvas.flush_events()

        sleep(.001)


def plot_axis(edges: Vec3DList):
    for vector in edges:
        edge_x = [point[0] for point in vector]
        edge_y = [point[1] for point in vector]
        edge_z = [point[2] for point in vector]

        ax.plot(edge_x, edge_y, edge_z, color=edges.color())


def get_octant_number(p: Point3D):
    if p[0] >= 0 and p[1] >= 0 and p[2] >= 0:
        return 1

    if p[0] >= 0 and p[1] < 0 and p[2] >= 0:
        return 2

    if p[0] >= 0 and p[1] < 0 and p[2] < 0:
        return 3

    if p[0] >= 0 and p[1] >= 0 and p[2] < 0:
        return 4

    if p[0] < 0 and p[1] >= 0 and p[2] >= 0:
        return 5

    if p[0] < 0 and p[1] < 0 and p[2] >= 0:
        return 6

    if p[0] < 0 and p[1] < 0 and p[2] < 0:
        return 7

    if p[0] < 0 and p[1] >= 0 and p[2] < 0:
        return 8


def check_octantes(edges: Vec3DList, at: Point3D):
    return get_octant_number(edges.center()) == get_octant_number(at)


if __name__ == "__main__":
    cube = solid.cube2(t=5)  # 0 -> 1
    sphere = solid.sphere2(t=10, color="magenta")  # 0 -> 1
    cylinder = solid.cylinder2(t=10, color="orange")  # 0 -> 1

    cube = transformation.translate_edges(cube, (7, 7, 7))
    sphere = transformation.translate_edges(sphere, (5, 5, 5))
    cylinder = transformation.translate_edges(cylinder, (2, 2, 2))

    cone = solid.cone2(1, t=10, color="cyan")
    toro = solid.toroide2(1, t=10, color="brown")
    cone = transformation.translate_edges(cone, (-7, -7, -7))
    toro = transformation.translate_edges(toro, (-5, -5, -5))

    cone = transformation.scale_solid(cone, (3, 3, 3))  # Cone is too small

    all_solids = [cube, sphere, cylinder, cone, toro]
    t1 = threading.Thread(target=main, args=[all_solids])
    t1.start()
    plt.show()
