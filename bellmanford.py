def bellman_ford(V, edges, S):
    dist = [float('inf')] * V
    dist[S] = 0

    for _ in range(V - 1):
        for u, v, wt in edges:
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt

    for u, v, wt in edges:
        if dist[u] != float('inf') and dist[u] + wt < dist[v]:
            return [-1]

    return dist

if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))

    edges = [list(map(int, input("Enter edge and weight (u v wt): ").split())) for _ in range(E)]
    start_node = int(input("Enter the start node: "))

    result = bellman_ford(V, edges, start_node)

    if result and result[0] != -1:
        print("\nShortest distances from the start node:")
        print(*result)  
    elif result[0] == -1:
        print("Graph contains a negative cycle.")
