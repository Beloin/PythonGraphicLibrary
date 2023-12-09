import numpy as np
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))

        return np.min(zs)


def draw_coordinate_system(ax, x=0, y=0, z=0, size=1):
    arrow_prop_dict = dict(mutation_scale=20, arrowstyle='->', shrinkA=0, shrinkB=0)

    a = Arrow3D([x, size], [y, 0], [z, 0], **arrow_prop_dict, color='r')
    ax.add_artist(a)
    a = Arrow3D([x, 0], [y, size], [z, 0], **arrow_prop_dict, color='b')
    ax.add_artist(a)
    a = Arrow3D([x, 0], [y, 0], [z, size], **arrow_prop_dict, color='g')
    ax.add_artist(a)

    # Give them a name:
    ax.text(0.0, 0.0, -0.1, r'$0$')
    ax.text(size + .1, 0, 0, r'$x$')
    ax.text(0, size + .1, 0, r'$y$')
    ax.text(0, 0, size + .1, r'$z$')
