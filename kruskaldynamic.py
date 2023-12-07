def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

def kruskalMST(vertices, edges):
    result = []
    i = 0
    e = 0
    edges = sorted(edges, key=lambda item: item[2])
    parent = [node for node in range(vertices)]
    rank = [0] * vertices

    while e < vertices - 1:
        u, v, w = edges[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e += 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    minimumCost = 0
    print("Edges in the constructed MST")
    for u, v, weight in result:
        minimumCost += weight
        print("%d -- %d == %d" % (u, v, weight))
    print("Minimum Spanning Tree", minimumCost)

if __name__ == '__main__':
    vertices = int(input("Enter the number of vertices: "))
    edges = []

    print("Enter edges and weights (u v w) for each edge (type 'done' when finished):")
    while True:
        edge_input = input().split()

        if edge_input[0].lower() == 'done':
            break

        u, v, w = map(int, edge_input)
        edges.append([u, v, w])

    kruskalMST(vertices, edges)
