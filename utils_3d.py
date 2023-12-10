import numpy as np
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

from types_3d import Point3D, Vector3D, X, Y, Z


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))

        return np.min(zs)


def draw_coordinate_system(ax, eye=None, size=1, txt="0"):
    arrow_prop_dict = dict(mutation_scale=20, arrowstyle='->', shrinkA=0, shrinkB=0)

    if not eye: eye = (0, 0, 0)

    a = Arrow3D([eye[X], eye[X] + size], [eye[Y], eye[Y]], [eye[Z], eye[Z]], **arrow_prop_dict, color='r')
    ax.add_artist(a)
    a = Arrow3D([eye[X], eye[X]], [eye[Y], eye[Y] + size], [eye[Z], eye[Z]], **arrow_prop_dict, color='b')
    ax.add_artist(a)
    a = Arrow3D([eye[X], eye[X]], [eye[Y], eye[Y]], [eye[Z], eye[Z] + size], **arrow_prop_dict, color='g')
    ax.add_artist(a)

    # Give them a name:
    ax.text(*eye, f'${txt}$')
    ax.text(eye[X] + size + .1, eye[Y], eye[Z], r'$x$')
    ax.text(eye[X], eye[Y] + size + .1, eye[Z], r'$y$')
    ax.text(eye[X], eye[Y], eye[Z] + size + .1, r'$z$')
