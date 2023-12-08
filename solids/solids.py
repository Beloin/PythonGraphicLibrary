import matplotlib.pyplot as plt
import numpy as np

from aux import linspace, plot, mesh_grid, vec2plot, addvec
from wireframe import Vec3DList


class Solid:

    def sphere(self, radius=1, t=20):
        theta1 = linspace(2 * np.pi, t)
        theta2 = linspace(np.pi, t)
        np.meshgrid()
        u, v = mesh_grid(theta1, theta2)

        x = radius * np.cos(u) * np.sin(v)
        y = radius * np.sin(u) * np.sin(v)
        z = radius * 2 * np.cos(v)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_aspect("equal")

        for i in range(t):
            ax.plot(x[:, i], y[:, i], z[:, i], color="black")
            ax.plot(x[i, :], y[i, :], z[i, :], color="black")

        plt.show()

    def sphere2(self, radius=1, t=20):
        theta1 = linspace(2 * np.pi, t)
        theta2 = linspace(np.pi, t)
        u, v = mesh_grid(theta1, theta2)

        x = radius * np.cos(u) * np.sin(v)
        y = radius * np.sin(u) * np.sin(v)
        z = radius * 2 * np.cos(v)

        vectors = []
        addvec(vectors, t, x, y, z)

        center = (0.0, 0.0, 0.0)

        vector3d = Vec3DList(vectors, t, center, "")

        # vec2plot(vector3d.raw())

        return vector3d

    def cube(self, size=2, t=10):
        theta = linspace(size, t)
        u, v = mesh_grid(theta, theta)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_aspect("equal")

        x = u
        y = v
        z = np.zeros_like(u)
        plot(x, y, z, t, ax)
        z = np.full_like(u, size)
        plot(x, y, z, t, ax)

        z = u
        x = v
        y = np.zeros_like(u)
        plot(x, y, z, t, ax)
        y = np.full_like(u, size)
        plot(x, y, z, t, ax)

        y = u
        z = v
        x = np.zeros_like(u)
        plot(x, y, z, t, ax)
        x = np.full_like(u, size)
        plot(x, y, z, t, ax)

        plt.show()

    def cube2(self, size=1, t=10):
        theta = linspace(size, t)
        u, v = mesh_grid(theta, theta)

        vectors = []

        x = u
        y = v
        z = np.zeros_like(u)
        addvec(vectors, t, x, y, z)
        z = np.full_like(u, size)
        addvec(vectors, t, x, y, z)

        z = u
        x = v
        y = np.zeros_like(u)
        addvec(vectors, t, x, y, z)
        y = np.full_like(u, size)
        addvec(vectors, t, x, y, z)

        y = u
        z = v
        x = np.zeros_like(u)
        addvec(vectors, t, x, y, z)
        x = np.full_like(u, size)
        addvec(vectors, t, x, y, z)

        center = (size / 2, size / 2, size / 2)

        vector3d = Vec3DList(vectors, 4, center, "")
        # vec2plot(vector3d.raw())

        return vector3d

    def cylinder(self, radius=1, t=20):

        height = 2 * radius

        u = linspace(2 * np.pi * radius, t)
        v = linspace(height, t)

        theta, z = mesh_grid(u, v)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_aspect("equal")

        plot(x, y, z, t, ax)

        for i in range(1, t + 1):
            x = (radius - (i / t)) * np.cos(u)
            y = (radius - (i / t)) * np.sin(u)

            z = np.zeros_like(u)
            ax.plot(x, y, z, linewidth=1, color="black")

            z = np.full_like(u, height)
            ax.plot(x, y, z, linewidth=1, color="black")

        for angle in u:
            x_line = [np.zeros_like(angle), radius * np.cos(angle)]
            y_line = [np.zeros_like(angle), radius * np.sin(angle)]
            z_line = np.zeros_like(angle)
            ax.plot(x_line, y_line, z_line, color='black')

            z_line = np.full_like(angle, height)
            ax.plot(x_line, y_line, z_line, color='black')

        plt.show()

    def cylinder2(self, radius=1, t=20):

        height = 2 * radius

        u = linspace(2 * np.pi * radius, t)
        v = linspace(height, t)

        theta, z = mesh_grid(u, v)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)

        vectors = []
        addvec(vectors, t, x, y, z)

        for angle in u:
            x_line = np.array([0, radius * np.cos(angle)])
            y_line = np.array([0, radius * np.sin(angle)])
            z_line = np.array([0, 0])

            vectors.append(((x_line[0], y_line[0], z_line[0]), (x_line[1], y_line[1], z_line[1])))

            z_line = np.array([height, height])

            vectors.append(((x_line[0], y_line[0], z_line[0]), (x_line[1], y_line[1], z_line[1])))

        center = (0.0, radius, 0.0)

        vector3d = Vec3DList(vectors, t, center, "")

        # vec2plot(vector3d.raw())

        return vector3d

    def cone(self, radius=1, t=20):

        height = 3 * radius

        theta = linspace(2 * np.pi, t)
        theta_h = linspace(height, t)

        u, v = mesh_grid(theta, theta_h)

        x = radius * np.cos(u) * (1 - v / height)
        y = radius * np.sin(u) * (1 - v / height)
        z = height * v / height

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_aspect("equal")

        plot(x, y, z, t, ax)

        for i in range(1, t + 1):
            x = (radius - (i / t)) * np.cos(theta)
            y = (radius - (i / t)) * np.sin(theta)
            z = np.zeros_like(theta)

            ax.plot(x, y, z, linewidth=1, color="black")

        for angle in theta:
            x_line = [np.zeros_like(angle), radius * np.cos(angle)]
            y_line = [np.zeros_like(angle), radius * np.sin(angle)]
            z_line = np.zeros_like(angle)
            ax.plot(x_line, y_line, z_line, color='black')

        plt.show()

    def cone2(self, radius=1, t=20):

        height = 3 * radius

        theta = linspace(2 * np.pi, t)
        theta_h = linspace(height, t)

        u, v = mesh_grid(theta, theta_h)

        x = radius * np.cos(u) * (1 - v / height)
        y = radius * np.sin(u) * (1 - v / height)
        z = height * v / height

        vectors = []
        addvec(vectors, t, x, y, z)

        for angle in theta:
            x_line = np.array([0, radius * np.cos(angle)])
            y_line = np.array([0, radius * np.sin(angle)])
            z_line = np.array([0, 0])

            vectors.append(((x_line[0], y_line[0], z_line[0]), (x_line[1], y_line[1], z_line[1])))

        center = (0.0, radius * 1.5, 0.0)

        vector3d = Vec3DList(vectors, t, center, "")

        # vec2plot(vector3d.raw())

        return vector3d

    def toroide(self, R=1, r=.7, t=20):
        theta = linspace(2 * np.pi, t)
        u, v = mesh_grid(theta, theta)

        x = (R + r * np.cos(v)) * np.cos(u)
        y = (R + r * np.cos(v)) * np.sin(u)
        z = r * np.sin(v)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_aspect("equal")

        plot(x, y, z, t, ax)

        plt.show()

    def toroide2(self, R=1, r=.7, t=20):
        theta = linspace(2 * np.pi, t)
        u, v = mesh_grid(theta, theta)

        x = (R + r * np.cos(v)) * np.cos(u)
        y = (R + r * np.cos(v)) * np.sin(u)
        z = r * np.sin(v)

        vectors = []
        addvec(vectors, t, x, y, z)

        center = (0.0, 0.0, 0.0)

        vector3d = Vec3DList(vectors, t, center, "")

        # vec2plot(vector3d.raw())

        return vector3d
