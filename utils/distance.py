from math import sqrt, ceil


def distance(origin: tuple, destination: tuple):
    dist = ceil(sqrt((origin[0] - destination[0]) ** 2 + (origin[1] - destination[1]) ** 2))
    return dist
