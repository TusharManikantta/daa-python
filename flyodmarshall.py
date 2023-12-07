def floyd_warshall():
    n = int(input("Enter the number of vertices: "))

    # Replace 'inf' with a large integer value
    inf_replacement = float('inf')  # or you can use a specific large value like 999999
    G = []

    # Take input for the adjacency matrix
    print("Enter the adjacency matrix (Enter INF for infinity):")
    for i in range(n):
        row = input().split()
        row = [inf_replacement if val.lower() == 'inf' else int(val) for val in row]
        G.append(row)               

    # Apply Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):  
            for j in range(n):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])

    # Print the resulting distances
    print("\nShortest distances between all pairs of vertices:")
    for i in range(n):
        for j in range(n):
            if G[i][j] == inf_replacement:
                print("INF", end="  ")
            else:
                print(G[i][j], end="  ")
        print()

# Example input:
# 4
# 0 3 INF 5
# 2 0 INF 4
# INF 1 0 INF
# INF INF 2 0

# Call the function
floyd_warshall()
    