import heapq
def spanningTree( V, adj):
    pq = [(0, 0)]  # (wt, node)
    vis = [0] * V
    total_weight = 0

    while pq:   
        wt, node = heapq.heappop(pq)
        if vis[node] == 1:
            continue

        vis[node] = 1
        total_weight += wt

        for neighbor in adj[node]:
            adjNode, edgeWeight = neighbor[0], neighbor[1]
            if not vis[adjNode]:
                heapq.heappush(pq, (edgeWeight, adjNode))

    return total_weight

if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    edges = []

    print("Enter edges and weights (u v w) for each edge:")
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])

    adj = [[] for _ in range(V)]

    for it in edges:
        adj[it[0]].append([it[1], it[2]])
        adj[it[1]].append([it[0], it[2]])

    result = spanningTree(V, adj)
    print("The sum of all the edge weights:", result)



