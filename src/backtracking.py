max_profit = -1


def knapsack_backtracking(items, W):
    global max_profit
    max_profit = -1

    items.sort(key=lambda item: item.proportional_value, reverse=True)

    knapsack_backtracking_internal(items, 0, 0, 0, W)

    return max_profit


def knapsack_backtracking_internal(items, level, profit, weight, W):
    global max_profit
    if weight <= W and profit > max_profit:
        max_profit = profit

    if level > len(items)-1:
        return

    if is_promising(items, level, weight, profit, W):
        knapsack_backtracking_internal(
            items, level + 1, profit + items[level].value, weight + items[level].weight, W)
        knapsack_backtracking_internal(items, level + 1, profit, weight, W)
    else:
        # print(f"{level} not promising")
        pass


def is_promising(items, level, weight, profit, W):
    if weight >= W:
        return False

    bound = profit
    total_weight = weight
    child = level

    while child < len(items) and total_weight + items[child].weight <= W:
        total_weight += items[child].weight
        bound += items[child].value
        child += 1

    if child < len(items):
        remaining_capacity = W - total_weight
        bound += remaining_capacity * items[child].proportional_value

    return bound > max_profit
