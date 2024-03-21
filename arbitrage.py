def arbitrage(exchange_rates):
    def log(x):

        # taylor expansion of natural log
        # math library was not working
        return x - x**2 / 2 + x**3 / 3 - x**4 / 4
    
    graph = {}
    for i, j, w in exchange_rates:
        if i not in graph:
            graph[i] = {}
        graph[i][j] = -log(w-1)

    n = len(graph)
    dist = {}
    prev = {}
    for node in graph:
        dist[node] = 999999999999
        prev[node] = None

    # make first node in graph dist 0
    dist[0] = 0

    for _ in range(n - 1):
        for u in graph:
            for v, w in graph[u].items():
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    prev[v] = u

    for u in graph:
        for v, w in graph[u].items():
            
            if dist[v] > dist[u] + w:
                cycle = [v]
                u = prev[v]
                while u != v:
                    cycle.append(u)
                    u = prev[u]
                cycle.append(v)

                if cycle[0] == cycle[-1]:
                    return cycle[::-1] 
    return None

exchange_rates = [(1, 2, 150), (2, 3, 0.006), (3, 1, 1.3)]
arbitrage_path = arbitrage(exchange_rates)
if arbitrage_path:
    print("Arbitrage path:", arbitrage_path)
else:
    print("No arbitrage opportunity.")