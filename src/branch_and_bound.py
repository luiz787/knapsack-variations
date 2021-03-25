from heapq import heapify, heappush, heappop

from item import Item
from branch_and_bound_node import BranchAndBoundNode


def knapsack_branch_and_bound(items, knapsack_capacity):
    items.sort(key=lambda item: item.proportional_value, reverse=True)

    heap = [BranchAndBoundNode(items, knapsack_capacity, -1, Item(0, 0))]
    heapify(heap)

    max_profit = 0
    while heap:
        current = heappop(heap)
        children_level = current.level + 1
        with_child = BranchAndBoundNode(items, knapsack_capacity, children_level, Item(current.item.weight +
                                                                                       items[children_level].weight, current.item.value + items[children_level].value))
        if with_child.item.weight <= knapsack_capacity and with_child.item.value > max_profit:
            max_profit = with_child.item.value

        if is_promising(with_child, knapsack_capacity, max_profit):
            heappush(heap, with_child)

        wout_child = BranchAndBoundNode(
            items, knapsack_capacity, children_level, current.item)
        if is_promising(wout_child, knapsack_capacity, max_profit):
            heappush(heap, wout_child)

    return max_profit


def is_promising(node, W, max_profit):
    if node.item.weight >= W:
        return False

    return node.bound > max_profit
