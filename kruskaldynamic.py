def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x], x, y = y, y, x
    elif rank[x] > rank[y]:
        parent[y], x, y = x, y, x
    else:
        parent[y], rank[x] = x, rank[x] + 1

def kruskalMST(vertices, edges):
    result, i, e = [], 0, 0
    edges.sort(key=lambda item: item[2])
    parent, rank = list(range(vertices)), [0] * vertices

    while e < vertices - 1:
        u, v, w = edges[i]
        i += 1
        x, y = find(parent, u), find(parent, v)
        if x != y:
            e += 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    minimumCost = sum(weight for u, v, weight in result)
    print("Edges in the constructed MST")
    for u, v, weight in result:
        print("%d -- %d == %d" % (u, v, weight))
    print("Minimum Spanning Tree:", minimumCost)

if __name__ == '__main__':
    vertices = int(input("Enter the number of vertices: "))
    edges = []

    print("Enter edges and weights (u v w) for each edge (type 'done' when finished):")
    while True:
        edge_input = input().split()

        if edge_input[0].lower() == 'done':
            break

        edges.append(list(map(int, edge_input)))

    kruskalMST(vertices, edges)
