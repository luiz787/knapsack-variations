import sys
import time

from backtracking import knapsack_backtracking
from branch_and_bound import knapsack_branch_and_bound
from item import Item


def main(args):
    if len(args) < 3:
        print("usage: python3 main.py kp_n_w_file (backtracking | branch_and_bound)")
        sys.exit(1)

    input = read_input(args[1])
    items = input[0]
    wmax = input[1]

    if args[2] == "backtracking":
        start = time.time()
        result = knapsack_backtracking(items, wmax)
        end = time.time()
        elapsed_time = end - start
        print(f"{elapsed_time:.8f};{result:.7g}")
    elif args[2] == "branch_and_bound":
        start = time.time()
        result = knapsack_branch_and_bound(items, wmax)
        end = time.time()
        elapsed_time = end - start
        print(f"{elapsed_time:.8f};{result:.7g}")


def read_input(file_name):
    items = []
    w_max = None
    with open(file_name, "r") as input_file:
        line = input_file.readline().strip().split()
        n = int(line[0])
        w_max = float(line[1])
        for _ in range(0, n):
            line = input_file.readline().split()
            v = float(line[0])
            w = float(line[1])
            item = Item(w, v)
            items.append(item)
    return (items, w_max)


if __name__ == "__main__":
    main(sys.argv)
