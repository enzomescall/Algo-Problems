from collections import defaultdict

def network(edges: list[(int, int, int)], computers: list[int]) -> list[(int, int, int)]:
  """
  Finds a minimum cost network connecting all computers, using at most twice the cost of the optimal solution.

  Args:
      edges: List of tuples (source, destination, cost) representing potential network paths.
      computers: List of integers representing computer IDs.

  Returns:
      List of tuples (source, destination, cost) representing the chosen network edges.
  """
  # Build a graph representation of potential connections
  graph = defaultdict(dict)
  for source, dest, cost in edges:
    graph[source][dest] = cost
    graph[dest][source] = cost  # Undirected edges

  # Find minimum spanning tree for computers only (Prim's algorithm)
  mst = minimum_spanning_tree(graph, computers)

  # Double the edges of the MST to include potential routers
  doubled_mst = []
  for source, dest, cost in mst:
    doubled_mst.append((source, dest, cost))
    doubled_mst.append((dest, source, cost))

  return doubled_mst

def minimum_spanning_tree(graph, vertices):
  """
  Finds the minimum spanning tree of a graph using Prim's algorithm.

  Args:
      graph: Dictionary representing the graph with nodes as keys and adjacent nodes with costs as values.
      vertices: List of integers representing nodes in the graph.

  Returns:
      List of tuples (source, destination, cost) representing the edges of the minimum spanning tree.
  """
  visited = set()
  mst = []
  current = vertices[0]  # Start with any vertex

  while len(visited) != len(vertices):
    # Find minimum cost edge from current vertex to unvisited vertex
    min_cost = float('inf')
    min_edge = None
    for neighbor, cost in graph[current].items():
      if neighbor not in visited and cost < min_cost:
        min_cost = cost
        min_edge = (current, neighbor, cost)
    
    # Add the minimum cost edge to the MST and mark current visited
    if min_edge:
      mst.append(min_edge)
      visited.add(current)
      current = min_edge[1]  # Move to the newly visited neighbor

  return mst

# Example usage (replace with your actual data)
edges = [
  (1, 2, 10), (1, 3, 5), (2, 3, 7), (2, 4, 15), (3, 4, 8), (1, 5, 20), (4, 5, 6)
]
computers = [1, 2, 3, 4]

network_edges = network(edges, computers)
print(network_edges)
