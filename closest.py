def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def minimum_distance(points):
    points.sort(key = lambda x: x[0])

    