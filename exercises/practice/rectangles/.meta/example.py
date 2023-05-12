import itertools


class Corners:
    def __init__(self, idx, jdx):
        # i, j are position of corner
        self.idx = idx
        self.jdx = jdx

    def __str__(self):
        return f'[{str(self.idx)}, {str(self.jdx)}]'


# return corner on the same line
def same_line(index, list_obj):
    return next((corner for corner in list_obj if corner.idx == index), None)


# return corner on the same column
def same_col(index, list_obj):
    return next((corner for corner in list_obj if corner.jdx == index), None)


def search_corners(list_obj):

    return [Corners(item, element) for item in range(len(list_obj))
            for element in range(len(list_obj[item]))
            if list_obj[item][element] == '+']


# validate that 4 points form a rectangle by
# comparing distance to centroid of the rectangle for all corners
def possible_rect(quartet):
    mid_x = 0
    mid_y = 0

    for centroid in quartet:
        mid_x = mid_x + centroid.idx / 4.0
        mid_y = mid_y + centroid.jdx / 4.0

    # reference distance using first corner
    dx = abs(quartet[0].idx - mid_x)
    dy = abs(quartet[0].jdx - mid_y)

    return not any(
        abs(quartet[idx].idx - mid_x) != dx
        or abs(quartet[idx].jdx - mid_y) != dy
        for idx in range(1, len(quartet))
    )


# validate path between two corners
def path(corner1, corner2, item):
    if corner1.idx == corner2.idx:
        return all(
            item[corner1.idx][jdx] in ['-', '+']
            for jdx in range(
                min(corner1.jdx + 1, corner2.jdx + 1),
                max(corner1.jdx, corner2.jdx),
            )
        )
    elif corner1.jdx == corner2.jdx:
        return all(
            item[idx][corner1.jdx] in ['|', '+']
            for idx in range(
                min(corner1.idx + 1, corner2.idx + 1),
                max(corner1.idx, corner2.idx),
            )
        )
    return None


# validate path of rectangle
def validate_rect(rectangle, item):
    # validate connection at every corner
    # with neighbours on the same line and col
    for idx, _ in enumerate(rectangle):
        line = same_line(rectangle[idx].idx, rectangle[:idx] + rectangle[idx + 1:])
        column = same_col(rectangle[idx].jdx, rectangle[:idx] + rectangle[idx + 1:])

        if not path(rectangle[idx], line, item) or not path(rectangle[idx], column, item):
            return False

    return True


# count number of rectangles inside ASCII in input lines
def rectangles(strings=''):
    rectangle_total = 0
    # test empty str
    if not strings:
        return rectangle_total

    corners = search_corners(strings)

    # no corners in str
    if not corners:
        return rectangle_total

    # all combinations of 4 corners
    quartets = list(itertools.combinations(corners, r=4))
    paths = (quartet for quartet in quartets if possible_rect(quartet))

    # validate paths
    for idx in paths:
        if validate_rect(idx, strings):
            rectangle_total += 1
    return rectangle_total
