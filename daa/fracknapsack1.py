def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    # Sort items by their value-to-weight ratio in descending order
    items.sort(reverse=True, key=lambda x: x[0])
    
    max_value = 0.0
    for ratio, weight, value in items:
        if capacity >= weight:
            # Take the whole item
            max_value += value
            capacity -= weight
        else:
            # Take a fraction of the item
            max_value += ratio * capacity
            break
    
    return max_value

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_value = fractional_knapsack(weights, values, capacity)
print("Maximum value (Fractional Knapsack):", max_value)

