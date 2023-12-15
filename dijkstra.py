import heapq

def dijkstra(adj, V, src):
    pq = [(0, src)]
    dist = [float('inf')] * V
    dist[src] = 0

    while pq:
        d, u = heapq.heappop(pq)

        for v, weight in adj[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    for i, d in enumerate(dist):
        print(f"{i} \t\t {d}")

if __name__ == "__main__":
    V, E = map(int, input("Enter the number of vertices and edges: ").split())
    adj = [[] for _ in range(V)]

    print("Enter edges and weights (u v w) for each edge:")
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    start_node = int(input("Enter the start node: "))
    dijkstra(adj, V, start_node)
