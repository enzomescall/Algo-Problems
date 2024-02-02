def maximals(P: list[tuple[int, int]]):
    A = []
    # Reverse sort the points by y-coordinate
    P.sort(key=lambda p: p[1], reverse=True)
    # Reverse sort the points by x-coordinate
    P.sort(key=lambda p: p[0], reverse=True)
    cutoff = P[0][1]
    A.append(P[0])
    for pair in P:
        if pair[1] > cutoff:
            A.append(pair)
            cutoff = pair[1]
    return A


# Example usage:
points = [(2,5),(5,4.7),(8,4.2),(10,3),(5.0, 3.0), (3.0, 3.0), (2.0, 1.0), (8.0, 1.0), (7.0, 3.0), (4.0, 2.0), (2.0, 4.0), (6.0, 2.0), (3.3, 4.3)]

print(maximals(points)) 


