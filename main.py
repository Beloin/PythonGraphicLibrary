import threading
from time import sleep

import matplotlib.pyplot as plt
import matplotlib

import random

import solids.solids as solids

import transformation

matplotlib.use('qtagg')

solid = solids.Solid()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


def configure():
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)
    ax.set_aspect("equal")


def main(cube=None):
    # World is -10 to 10
    at = (0, 0, 0)
    eye = (5, 0, 5)

    cube = transformation.scale_solid(cube, (4, 4, 4))
    while True:
        cube = transformation.rotate_solid(cube, (3, 3, 3))

        ax.clear()
        configure()
        plot_axis(cube)

        fig.canvas.draw()
        fig.canvas.flush_events()

        sleep(.001)


def plot_axis(edges):
    for vector in edges:
        edge_x = [point[0] for point in vector]
        edge_y = [point[1] for point in vector]
        edge_z = [point[2] for point in vector]

        ax.plot(edge_x, edge_y, edge_z, color="black")


if __name__ == "__main__":
    cube = solid.cube2(t=2)  # 0 -> 1
    t1 = threading.Thread(target=main, kwargs={'cube': cube})
    t1.start()
    plt.show()
    # t1.join()
