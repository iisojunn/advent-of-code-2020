"""Day 3 advent of code 2020"""

from itertools import islice
from math import prod


def read_input(name):
    with open(name, "r") as input_file:
        data = input_file.read().splitlines()
        print(f"Input data: {data}")
        return data


def trees_on_the_path(tree_map, right, down):
    encountered_trees = 0
    index = 0
    for line in islice(tree_map, down, None, down):
        index = (index + right) % len(line)
        if line[index] == "#":
            encountered_trees += 1
    print(f"Encountered {encountered_trees} trees with right {right} and "
          f"down {down}")
    return encountered_trees


def trees_on_multiple_paths(tree_map, paths):
    encountered_trees = []
    for right, down in paths:
        encountered_trees.append(trees_on_the_path(tree_map, right, down))
    return encountered_trees


if __name__ == '__main__':
    TREE_MAP = read_input("input")
    print(f"Encountered total {trees_on_the_path(TREE_MAP, 3, 1)} trees.")
    print()

    PATHS = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = trees_on_multiple_paths(TREE_MAP, PATHS)
    print(f"Product of trees encountered on multiple paths {prod(trees)}")
