"""Day 3 advent of code 2020"""


def read_input():
    with open("input", "r") as input_file:
        data = input_file.read().splitlines()
        print(f"Input data: {data}")
        return data


def count_trees():
    encountered_trees = 0
    index = 0
    for line in read_input()[1:]:
        index = (index + 3) % len(line)
        if line[index] == "#":
            encountered_trees += 1
    return encountered_trees


if __name__ == '__main__':
    print(f"Encountered total {count_trees()} trees.")

