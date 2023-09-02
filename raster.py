import math


Scale = tuple[int, int]
Point = tuple[float, float]
Vector = tuple[Point, Point]

"""
Always P2 >= P1
"""


def scale2d_interval(vec: Vector, scale: Scale, rmin=-1, rmax=1, scale_y: Scale = None) -> Vector:
    # 0 -> 1
    # s1 -> s2
    # You need to scale X and then Y (or vice versa)
    # https://stats.stackexchange.com/questions/281162/scale-a-number-between-a-range ?

    svec = []

    if not scale_y:
        scale_y = scale

    for point in vec:
        x = point[0]
        xs = (x - rmin) / (rmax - rmin)
        xs *= (scale[1] - scale[0])
        xs += scale[0]

        y = point[1]
        ys = (y - rmin) / (rmax - rmin)
        ys *= (scale_y[1] - scale_y[0])
        ys += scale_y[0]

        svec.append((xs, ys))

    return tuple(svec)


def create_frag(fragls: list[tuple[float, float]], x: float, y: float):
    xm = math.floor(x)
    ym = math.floor(y)
    fragls.append((xm + .5, ym + .5))


# TODO: Is this interpolation?
def raster(vec: Vector, scale: Scale, scale_y: Scale = None):
    """
    Raster o Vector using the equation of a line: `y = m*x + b`

    :param vec should be normalized between 0 and 1
    :param scale

    :return list of points that should be painted (based on the "middle" of the point)
    """
    vec = scale2d_interval(vec, scale, 0, 1, scale_y)

    fragls: list[Point] = []

    dx = vec[1][0] - vec[0][0]
    dy = vec[1][1] - vec[0][1]

    if not dx:
        m = 0
    else:
        m = dy / dx

    x = vec[0][0]
    y = vec[0][1]

    b = y - m * x
    if math.fabs(dx) > math.fabs(dy):
        create_frag(fragls, x, y)
        while x < vec[1][0]:
            x += 1
            y = m * x + b
            create_frag(fragls, x, y)
    else:
        create_frag(fragls, x, y)
        while y < vec[1][1]:
            y += 1
            x = (y - b) / m
        create_frag(fragls, x, y)

    return fragls


def scale2d(sx, sy):
    mx = [[sx, 0], [sy, 0]]
    pass  # TODO: Complete this scale


def pretty_printmx(mx):
    for line in mx:
        print("| ", end='')
        for v in line:
            print(v, end=' ')
        print("|")


def main():
    test_vector: Vector = (0, 0), (0.2, 0.1)
    vector_9x9: Vector = (0, 0), (1.8, .9)

    # Assert scaled_vector
    scaled_vec = scale2d_interval(test_vector, (0, 9), rmin=0)
    assert scaled_vec == vector_9x9

    scale = 10
    scale_y = 20
    norm_vec: Vector = (.2, .3), (.8, .7)
    mx = [[0 for _ in range(scale)] for _ in range(scale_y)]
    points = raster(norm_vec, (0, scale), (0, scale_y))

    for x, y in points:
        x = math.floor(x)
        y = math.floor(y)
        mx[y][x] = 1

    pretty_printmx(mx)


if __name__ == '__main__':
    main()
