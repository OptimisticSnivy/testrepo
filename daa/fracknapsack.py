# Define a class to represent an item
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # value-to-weight ratio


# Function to perform fractional knapsack
def fractional_knapsack(capacity, items):
    # Sort items based on value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0  # Total value of knapsack
    for item in items:
        if capacity == 0:  # If knapsack is full, break
            break

        # If the item can be completely added
        if item.weight <= capacity:
            total_value += item.value
            capacity -= item.weight
        else:
            # If only part of the item can be added
            total_value += item.value * (capacity / item.weight)
            capacity = 0  # Knapsack is full

    return total_value


# Example usage
if __name__ == "__main__":
    items = [Item(20, 10), Item(100, 10), Item(120, 20)]
    capacity = 50  # Knapsack capacity

    # Calculate maximum value
    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in knapsack: {max_value}")
