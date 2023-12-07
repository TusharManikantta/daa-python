def bellman_ford():
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))

    edges = []
    print("Enter edges and weights (u v wt) for each edge:")
    for _ in range(E):
        edge_input = list(map(int, input().split()))
        edges.append(edge_input)

    S = int(input("Enter the start node: "))

    dist = [float('inf')] * V
    dist[S] = 0

    for i in range(V - 1):
        for edge in edges:
            u, v, wt = edge
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt

    for edge in edges:
        u, v, wt = edge
        if dist[u] != float('inf') and dist[u] + wt < dist[v]:
            print("Graph contains a negative cycle.")
            return [-1]

    return dist

if __name__ == "__main__":
    dist = bellman_ford()

    if dist and dist[0] != -1:
        print("\nShortest distances from the start node:")
        for d in dist:
            print(d, end=" ")
