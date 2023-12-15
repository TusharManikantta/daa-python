INF = float('inf')

def floyd_warshall(n, G):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    print_solution(G)

def print_solution(distance):
    for i in range(len(distance)):
        for j in range(len(distance[i])):
            print(distance[i][j], end="  ")
        print(" ")

# Get the size of the graph from the user
n = int(input("Enter the number of vertices in the graph: "))

# Get the adjacency matrix from the user
G = []
print("Enter the adjacency matrix (INF for infinity):")
for i in range(n):
    row = list(map(float, input().split()))
    G.append(row)

# Call the Floyd-Warshall algorithm with the user-provided graph
floyd_warshall(n, G)

# # Example input:
# # 4
# # 0 3 INF 5
# # 2 0 INF 4
# # INF 1 0 INF
# # INF INF 2 0



