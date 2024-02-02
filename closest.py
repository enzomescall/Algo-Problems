def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5



def minimum_distance(points):
    points.sort(key = lambda x: x[0])
    return close_x(points, 0, len(points) - 1)

def close_x(points, left, right):
    if right - left <= 3:
        return brute_force(points, left, right)
    mid = (left + right) // 2
    left_min = close_x(points, left, mid)
    right_min = close_x(points, mid + 1, right)
    
    
    # Check for points that are close to the middle line
    min_distance = min(left_min, right_min)
    mid_x = points[mid][0]

    strip = [] # Points within min_distance of the middle line
    for point in points[left:right + 1]:
        if abs(point[0] - mid_x) < min_distance:
            strip.append(point)
    
    min_distance = strip_close(strip, len(strip), min_distance)

    return min_distance

def strip_close(strip, n, min_distance):
    strip.sort(key = lambda x: x[1])
    for i in range(n):
        j = i + 1
        while j < n and (strip[j][1] - strip[i][1]) < min_distance:
            min_distance = min(min_distance, distance(strip[i], strip[j]))
            j += 1
    return min_distance

def brute_force(points, left, right):
    min_distance = float('inf')
    for i in range(left, right):
        for j in range(i + 1, right + 1):
            d = distance(points[i], points[j])
            if d < min_distance:
                min_distance = d
    return min_distance