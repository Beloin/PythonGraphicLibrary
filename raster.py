import math
from typing import List, Tuple

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


def raster(vec: Vector, scale: Scale):
    """
    Raster a Vector using the equation of a line: `y = m*x + b`

    :param vec should be normalized between 0 and 1
    :param scale the Cols X Lines

    :return list of points that should be painted (based on the "middle" of the point)
    """
    vec = scale2d_interval(vec, scale, -1, 1)  # Normalize to -1 and 1

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

    if dx == 0:
        m = 0
    else:
        m = dy / dx

    x = x1
    y = y1

    b = y - m * x
    if math.fabs(dx) > math.fabs(dy):
        create_frag(fragls, x, y)
        if x > x2:
            x, x2 = x2, x
        while x < x2:
            x += 1
            y = m * x + b
            create_frag(fragls, x, y)
    else:
        create_frag(fragls, x, y)
        if y > y2:
            y, y2 = y2, y
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


# TODO: Change to Edge list instead of vertex list
def draw_polygon(vlist: list[Point], scale: Scale) -> list[Point]:
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


def fill_polygon(polygon: list[Point], scale: Scale):
    temp_mx = [[0 for _ in range(scale[0])] for _ in range(scale[1])]
    insert_points(temp_mx, polygon)
    new_pts = []
    for line in range(len(temp_mx)):
        in_count = 0
        to_be = []
        for column in range(len(temp_mx[line])):
            if temp_mx[line][column]:
                if column > 0 and (not temp_mx[line][column - 1]):
                    in_count += 1

            if in_count % 2:
                to_be.append((column, line))

        if in_count % 2 == 0:
            new_pts.extend(to_be)

    polygon.extend(new_pts)

    return polygon


def insert_points(mx, points):
    for x, y in points:
        x = math.floor(x)
        y = math.floor(y)

        if (y > 0 and x > 0) and (y < len(mx) and x < len(mx[0])):
            mx[y][x] = 1


def generate_hermite_point(p1: Point, p2: Point, t1, t2, t: float) -> Point:
    # P(t) = THGh
    # Will be implemented into parts. Expanding the Linear Algebra
    pt0 = 2 * (t * t * t) - 3 * (t * t) + 1
    pt1 = -2 * (t * t * t) + 3 * (t * t)
    pt2 = (t * t * t) - 2 * (t * t) + t
    pt3 = (t * t * t) - (t * t)

    x = pt0 * p1[0] + pt1 * p2[0] + pt2 * t1[0] + pt3 * t2[0]
    y = pt0 * p1[1] + pt1 * p2[1] + pt2 * t1[1] + pt3 * t2[1]

    return x, y


def insert_hermite(mx, scale: Scale, p1, p2, t1, t2, step=.1, qtn: int = None):
    ptx = get_hermite_points(scale, p1, p2, t1, t2, step, qtn)
    insert_points(mx, ptx)


def get_hermite_points(scale: Scale, p1, p2, t1, t2, step=.1, qtn: int = None):
    points: list[Point] = []
    if qtn:
        step = 1 / qtn
    t = 0
    while t <= 1:
        point = generate_hermite_point(p1, p2, t1, t2, t)
        points.append(point)
        t += step
    vectors: list[Vector] = []
    for i in range(1, len(points)):
        pa = points[i - 1]
        pp = points[i]
        vectors.append((pa, pp))
    ptx = []
    for vec in vectors:
        ts = raster(vec, scale)
        ptx.extend(ts)
    return ptx


def main3():
    scale_x = 100
    scale_y = 100

    p1, p2 = (.1, .2), (.1, .6)
    t1, t2 = (.5, .5), (.5, .5)
    mx = [[0 for _ in range(scale_x)] for _ in range(scale_y)]
    insert_hermite(mx, (scale_x, scale_y), p1, p2, t1, t2)

    pretty_printmx(mx)


def main2():
    scale = (600, 100)
    mx = [[0 for _ in range(scale[0])] for _ in range(scale[1])]
    #           (.2, .2)
    #
    #  (.0, .0)            (.4, .0)
    #           (.2, -.2)
    triangle = [(.0, .0), (.2, .2), (.4, .0), (.2, -.2)]
    polygon = draw_polygon(triangle, scale)
    fill_polygon(polygon, scale)

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
    # main2()
    main3()
