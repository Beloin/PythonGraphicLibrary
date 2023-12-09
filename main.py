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
        item.update(transformation.scale_solid(item, (3, 3, 3)))

    # cube = transformation.scale_solid(cube, (4, 4, 4))
    while True:

        ax.clear()
        configure()
        for item in solid_list:
            item.update(transformation.rotate_solid(item, (0, 0, 0)))
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

    cube = transformation.translate_edges(cube, (5, 5, 5))
    # sphere = transformation.translate_edges(sphere, (5, 5, 5))
    t1 = threading.Thread(target=main, args=[[cube, sphere]])
    t1.start()
    plt.show()
    # t1.join()
