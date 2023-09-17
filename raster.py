import math

Scale = tuple[int, int]
"""
Scale: Cols x Lines
"""

Point = tuple[float, float]

Vector = tuple[Point, Point]
"""
Always P2 >= P1
"""


def scale2d_interval(vec: Vector, scale: Scale, rmin=-1, rmax=1) -> Vector:
    # 0 -> 1
    # s1 -> s2
    # You need to scale X and then Y (or vice versa)
    # https://stats.stackexchange.com/questions/281162/scale-a-number-between-a-range ?

    svec = []

    scale_x, scale_y = scale
    for point in vec:
        x = point[0]
        xs = (x - rmin) / (rmax - rmin)
        xs *= scale_x - 0
        xs += 0

        y = point[1]
        ys = (y - rmin) / (rmax - rmin)
        ys *= scale_y - 0
        ys += 0

        svec.append((xs, ys))

    return tuple(svec)


def create_frag(fragls: list[tuple[float, float]], x: float, y: float):
    xm = math.floor(x)
    ym = math.floor(y)
    fragls.append((xm + 0.5, ym + 0.5))


# TODO: Is this interpolation?
def raster(vec: Vector, scale: Scale):
    """
    Raster o Vector using the equation of a line: `y = m*x + b`

    :param vec should be normalized between 0 and 1
    :param scale the Cols X Lines

    :return list of points that should be painted (based on the "middle" of the point)
    """
    vec = scale2d_interval(vec, scale, 0, 1)  # Normalize to -1 and 1

    fragls: list[Point] = []

    x1 = vec[0][0]
    x2 = vec[1][0]

    y1 = vec[0][1]
    y2 = vec[1][1]

    if x1 > x2 or y1 > y2:
        x1, x2 = x2, x1
        y1, y2, = y2, y1

    dx = x2 - x1
    dy = y2 - y1

    if not dx:
        m = 0
    else:
        m = dy / dx

    x = x1
    y = y1

    b = y - m * x
    if math.fabs(dx) > math.fabs(dy):
        create_frag(fragls, x, y)
        while x < x2:
            x += 1
            y = m * x + b
            create_frag(fragls, x, y)
    else:
        create_frag(fragls, x, y)
        while y < y2:
            y += 1
            if m != 0:
                x = (y - b) / m
            create_frag(fragls, x, y)

    return fragls


def pretty_printmx(mx):
    for line in mx:
        print("| ", end='')
        for v in line:
            print(v, end=' ')
        print("|")


def convert_img(matrix):
    mx2 = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for line in range(len(matrix)):
        for column in range(len(matrix[line])):
            line_index = (len(matrix) - 1) - line
            mx2[line_index][column] = matrix[line][column]
    return mx2


def draw_polygon(vlist: list[Point], scale: Scale):
    pxs = []
    length = len(vlist)
    for i in range(length):
        if i < length - 1:
            final = i + 1
        else:
            final = 0

        vx = (vlist[i], vlist[final])

        points = raster(vx, scale)
        pxs.extend(points)

    return pxs


def fill_polygon(ppoints: list[tuple[int, int]], scale: Scale):

    pass


def insert_points(mx, points):
    for x, y in points:
        x = math.floor(x)
        y = math.floor(y)
        if len(mx) > y and len(mx[0]) > x:
            mx[y][x] = 1


def main2():
    scale = (20, 20)
    mx = [[0 for _ in range(scale[0])] for _ in range(scale[1])]
    #           (.2, .2)
    #
    #  (.0, .0)            (.4, .0)
    triangle = [(.0, .0), (.2, .2), (.4, .0)]
    polygon = draw_polygon(triangle, scale)

    insert_points(mx, polygon)
    pretty_printmx(mx)


def main():
    test_vector: Vector = (0, 0), (0.2, 0.1)
    vector_9x9: Vector = (0, 0), (1.8, 0.9)

    # Assert scaled_vector
    scaled_vec = scale2d_interval(test_vector, (9, 9), rmin=0)
    assert scaled_vec == vector_9x9

    scale_x = 10
    scale_y = 10
    # norm_vec: Vector = (.2, .3), (.8, .7)
    norm_vec: Vector = (0.3, 0), (1, 1)
    mx = [[0 for _ in range(scale_x)] for _ in range(scale_y)]
    points = raster(norm_vec, (scale_x, scale_y))

    insert_points(mx, points)

    pretty_printmx(mx)

    c_mx = convert_img(mx)
    pretty_printmx(c_mx)


if __name__ == "__main__":
    # main()
    main2()
