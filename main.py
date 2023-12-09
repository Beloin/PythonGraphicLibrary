import threading
from time import sleep

import matplotlib.pyplot as plt
import matplotlib

import random

import solids.solids as solids

import transformation
from wireframe import Vec3DList

matplotlib.use('qtagg')

solid = solids.Solid()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
run = True


def configure():
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)
    ax.set_aspect("equal")


def main(solid_list):
    # World is -10 to 10
    at = (0, 0, 0)
    eye = (5, 0, 5)

    for item in solid_list:
        item.update(transformation.scale_solid(item, (2, 2, 2)))

    while run:

        ax.clear()
        configure()
        for item in solid_list:
            item.update(transformation.rotate_solid(item, (10, 0, 10)))
            plot_axis(item)

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
    cube = solid.cube2(t=2)  # 0 -> 1
    sphere = solid.sphere2(t=10, color="red")  # 0 -> 1
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
