"""Day 5 advent of code 2020"""


def read_input():
    with open("input", "r") as input_data:
        return input_data.read().splitlines()


def fb_to_01(binary_row):
    return binary_row.replace("F", "0").replace("B", "1")


def row_number(binary_row):
    values = [64, 32, 16, 8, 4, 2, 1]
    return sum(int(binary) * value for binary, value
                    in zip(binary_row, values))


def lr_to_01(binary_column):
    return binary_column.replace("L", "0").replace("R", "1")


def column_number(binary_column):
    values = [4, 2, 1]
    return sum(int(binary) * value for binary, value
                    in zip(binary_column, values))


def calculate_seat_id(boarding_pass):
    return row_number(fb_to_01(boarding_pass[:7])) * 8 \
           + column_number(lr_to_01(boarding_pass[7:]))


def find_my_seat(seats):
    for seat_id in range(128 * 8):
        if is_my_seat(seat_id, seats):
            return seat_id


def is_my_seat(seat_id, seats):
    seat_not_reserved = seat_id not in seats
    neighbour_seats_reserved = seat_id - 1 in seats and seat_id + 1 in seats
    return seat_not_reserved and neighbour_seats_reserved


if __name__ == '__main__':
    seat_ids = [calculate_seat_id(boarding_pass) for boarding_pass in
                read_input()]
    seat_ids.sort(reverse=True)
    print(f"Highest seat_id {seat_ids[0]}")
    print(f"My seat {find_my_seat(seat_ids)}")
