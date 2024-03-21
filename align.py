import itertools

def align(seriesA: list[(int, int)], seriesB: list[(int, int)]):
    def dist(a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    
    m = len(seriesA)
    mrange = range(1, m)
    n = len(seriesB)
    nrange = range(1, n)

    C = [[0 for _ in range(m)] for _ in range(n)]
    C[0][0] = dist(seriesA[0], seriesB[0])

    for j in mrange:
        C[0][j] = C[0][j - 1] + dist(seriesA[j], seriesB[0])

    for i in nrange:
        C[i][0] = C[i - 1][0] + dist(seriesA[0], seriesB[i])

    for j, i in itertools.product(mrange, nrange):
        d = dist(seriesA[j], seriesB[i])
        C[i][j] = min(C[i - 1][j] + d,
                        C[i][j - 1] + d,
                        C[i - 1][j - 1] + d)

    return C[n - 1][m - 1]