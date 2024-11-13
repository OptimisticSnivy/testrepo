def knapsack(wts, values, capacity):
    n = len(wts)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if wts[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - wts[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]


# Example usage
weights = [1, 2, 3, 4]
values = [10, 20, 30, 40]
capacity = 5
max_value = knapsack(weights, values, capacity)
print("Maximum value:", max_value)
