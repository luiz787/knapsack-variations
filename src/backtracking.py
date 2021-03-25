max_profit = -1


def knapsack_backtracking(items, knapsack_capacity):
    global max_profit
    max_profit = -1

    items.sort(key=lambda item: item.proportional_value, reverse=True)

    knapsack_backtracking_internal(items, 0, 0, 0, knapsack_capacity)

    return max_profit


def knapsack_backtracking_internal(items, level, profit, weight, knapsack_capacity):
    global max_profit
    if weight <= knapsack_capacity and profit > max_profit:
        max_profit = profit

    if level > len(items)-1:
        return

    if is_promising(weight, knapsack_capacity):
        knapsack_backtracking_internal(
            items, level + 1, profit + items[level].value, weight + items[level].weight, knapsack_capacity)
        knapsack_backtracking_internal(
            items, level + 1, profit, weight, knapsack_capacity)


def is_promising(weight, knapsack_capacity):
    return weight < knapsack_capacity
