import threading
from time import sleep

import matplotlib.pyplot as plt
import matplotlib

import solids.solids as solids

import transformation
from utils_3d import draw_coordinate_system, draw_coordinate_system
from wireframe import Vec3DList

from camera_persp import camera

matplotlib.use('qtagg')

solid = solids.Solid()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
run = True


def configure():
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)
    ax.set_aspect("equal")

    draw_coordinate_system(ax, size=10)


def main(solid_list):
    # World is -10 to 10
    at = (5, 5, 5)
    eye = (5, -5, 5)
    cam = camera.get_camera(at, eye)

    eye_rep = solid.sphere2(color="red")  # 0 -> 1
    eye_rep = transformation.translate_edges(eye_rep, eye)

    for item in solid_list:
        item.update(transformation.scale_solid(item, (2, 2, 2)))

    print(cam)
    while run:

        ax.clear()
        configure()
        # Eye coordinate System
        draw_coordinate_system(ax, eye, size=5, txt="eye")
        for item in solid_list:
            item.update(transformation.rotate_solid(item, (10, 0, 10)))
            plot_axis(item)

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
    run = False
