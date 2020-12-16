"""Day 13 Advent of code 2020"""


def read_input():
    with open("input", "r") as input_file:
        notes = input_file.read().splitlines()
        return int(notes[0]), notes[1]


def parse_schedule(schedule):
    buses = [int(bus_id) for bus_id in schedule.split(",") if bus_id != "x"]
    return sorted(buses)


def resolve_bus_and_wait_time(depart, schedule):
    wait_times = [bus_id - (depart % bus_id) for bus_id in schedule]
    min_wait_time = min(wait_times)
    bus_id = schedule[wait_times.index(min_wait_time)]
    return min_wait_time, bus_id


def search_t(requirements):
    cycle, time = requirements.pop(0)
    for bus_id, offset in requirements:
        time = resolve_time(time, cycle, bus_id, offset)
        cycle *= bus_id
    return time


def resolve_time(time, addition, divisor, offset):
    while True:
        if divisor - (time % divisor) == offset:
            return time
        time += addition


def bus_requirements(schedule):
    return [(int(bus_id), offset % int(bus_id)) for offset, bus_id in
            enumerate(schedule.split(",")) if bus_id != "x"]


if __name__ == '__main__':
    depart_time, bus_schedule = read_input()
    bus, wait = resolve_bus_and_wait_time(depart_time,
                                          parse_schedule(bus_schedule))
    print(f"Earliest bus id multiplied by wait time {bus * wait}")

    t = search_t(bus_requirements(bus_schedule))
    print(f"Timestamp t filling the requirements is {t}")
