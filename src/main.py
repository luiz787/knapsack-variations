from backtracking import knapsack_backtracking


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.proportional_value = value / weight


def main():
    input = read_input()
    items = input[0]
    wmax = input[1]

    print(knapsack_backtracking(items, wmax))


def read_input():
    items = []

    line = input().split()
    n = int(line[0])
    w_max = int(line[1])

    for _ in range(0, n):
        line = input().split()
        v = int(line[0])
        w = int(line[1])
        item = Item(w, v)
        items.append(item)

    return (items, w_max)


if __name__ == "__main__":
    main()
