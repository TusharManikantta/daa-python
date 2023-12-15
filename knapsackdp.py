def knapsack(weights, profits, max_weight):
  dp = [0] * (max_weight + 1)
  for i in range(len(profits)):
    for j in range(max_weight, -1, -1): 
      if weights[i] <= j:
        dp[j] = max(dp[j], dp[j - weights[i]] + profits[i])

  return dp[max_weight]

max_weight = int(input("Enter the max weight: "))
profits = list(map(int, input("Enter the profit array: ").split()))
weights = list(map(int, input("Enter the weight array: ").split()))

print(knapsack(weights, profits, max_weight))   