"""Day 13 Advent of code 2020"""


def read_input():
    with open("input", "r") as input_file:
        notes = input_file.read().splitlines()
        return int(notes[0]), parse_schedule(notes[1])


def parse_schedule(notes):
    buses = [int(bus_id) for bus_id in notes.split(",") if bus_id != "x"]
    return sorted(buses)


def resolve_bus_id_and_wait_time(depart, schedule):
    wait_times = [bus_id - (depart % bus_id) for bus_id in schedule]
    min_wait_time = min(wait_times)
    bus_id = schedule[wait_times.index(min_wait_time)]
    return min_wait_time, bus_id


if __name__ == '__main__':
    depart_time, bus_schedule = read_input()
    bus, wait = resolve_bus_id_and_wait_time(depart_time, bus_schedule)
    print(f"Earliest bus id multiplied by wait time {bus * wait}")
