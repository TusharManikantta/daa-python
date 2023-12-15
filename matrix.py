import sys

dp = [[-1 for i in range(100)] for j in range(100)]

def matrixChainMemoised(p, i, j):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = sys.maxsize
    for k in range(i, j):
        dp[i][j] = min(dp[i][j], matrixChainMemoised(p, i, k) + matrixChainMemoised(p, k + 1, j) + p[i - 1] * p[k] * p[j])
    return dp[i][j]

def MatrixChainOrder(p, n):
    i = 1
    j = n - 1   
    return matrixChainMemoised(p, i, j)

# Example of taking dynamic input
n = int(input("Enter the number of matrices: "))
arr = [int(x) for x in input("Enter the dimensions of matrices separated by space: ").split()]

result = MatrixChainOrder(arr, n)
print("Minimum number of multiplications is", result)