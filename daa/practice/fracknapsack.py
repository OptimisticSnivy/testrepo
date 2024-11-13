class Item:
    def __init__(self, value, wt):
        self.value = value
        self.wt = wt
        self.ratio = value / wt  # value/weight ratio


def frac_knapsack(cap, items):
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0
    for item in items:
        if cap == 0:
            break

        if item.wt <= cap:
            total_value += item.value
            cap -= item.wt
        else:
            total_value += item.value * (cap / item.wt)
            cap = 0

    return total_value


if __name__ == "__main__":
    items = [Item(20, 10), Item(100, 10), Item(120, 20)]
    cap = 50

    max_value = frac_knapsack(cap, items)
    print(f"Maximum value in knapsack: {max_value}")
