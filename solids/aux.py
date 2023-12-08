import matplotlib.pyplot as plt
import numpy as np


def plot(x, y, z, t, ax):
    for i in range(t):
        ax.plot(x[:, i], y[:, i], z[:, i], color="black")
        ax.plot(x[i, :], y[i, :], z[i, :], color="black")


def addvec(vectors, t, x, y, z):
    for i in range(t):
        for j in range(len(x) - 1):
            edge = (
                (x[j, i], y[j, i], z[j, i]),
                (x[j + 1, i], y[j + 1, i], z[j + 1, i])
            )
            vectors.append(edge)

        for j in range(len(x[i]) - 1):
            edge = (
                (x[i, j], y[i, j], z[i, j]),
                (x[i, j + 1], y[i, j + 1], z[i, j + 1])
            )
            vectors.append(edge)
    return vectors


def vec2plot(vectors):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect("equal")

    for vector in vectors:
        edge_x = [point[0] for point in vector]
        edge_y = [point[1] for point in vector]
        edge_z = [point[2] for point in vector]

        ax.plot(edge_x, edge_y, edge_z, color="black")

    plt.show()


def mesh_grid(theta1, theta2):
    u = np.zeros((len(theta1), len(theta2)))
    v = np.zeros((len(theta1), len(theta2)))

    for i in range(len(theta1)):
        u[i, :] = theta1[i]

    for j in range(len(theta2)):
        v[:, j] = theta2[j]

    return u, v


def linspace(stop, num):
    theta = np.zeros(num)
    for i in range(num):
        theta[i] = stop * i / (num - 1)
    return theta
