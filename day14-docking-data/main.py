"""Day 14 Advent of code"""
from itertools import product


def read_input():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def instructions(init_script):
    mask = ""
    commands = []
    for row in init_script:
        if row.startswith("mask"):
            if commands:
                yield mask, commands
                commands = []
            mask = row.split(" = ")[1]
        else:
            commands.append(parse_mem_command(row))
    yield mask, commands


def parse_mem_command(row):
    mem, value = row.replace("mem[", "").replace("]", "").split(" = ")
    return {"mem": int(mem), "value": int(value)}


def convert_to_bits(value):
    if not value:
        value = 0
    return '{0:036b}'.format(value)


def apply_mask_to_bit(mask_bit, value_bit):
    if mask_bit == "X":
        return value_bit
    return mask_bit


def masked_value(mask, value):
    new_value = [apply_mask_to_bit(mask_bit, value_bit)
                 for mask_bit, value_bit in zip(mask, convert_to_bits(value))]
    return int("".join(new_value), 2)


def execute(init_script):
    memory = {}
    for mask, commands in instructions(init_script):
        for cmd in commands:
            memory[cmd["mem"]] = masked_value(mask, cmd["value"])
    return memory


def apply_mask_to_mem_bit(mask_bit, mem_bit):
    if mask_bit in "1X":
        return mask_bit
    return mem_bit


def masked_addresses(mask, memory):
    floating_address = get_floating_address(mask, memory)
    for floating_bits in product('10', repeat=floating_address.count("X")):
        address = floating_address
        for bit in floating_bits:
            address = address.replace("X", bit, 1)
        yield int(address, 2)


def get_floating_address(mask, memory):
    address = [apply_mask_to_mem_bit(mask_bit, mem_bit) for mask_bit, mem_bit
               in zip(mask, convert_to_bits(memory))]
    return "".join(address)


def execute_v2(init_script):
    memory = {}
    for mask, commands in instructions(init_script):
        for cmd in commands:
            addresses = masked_addresses(mask, cmd["mem"])
            for mem in addresses:
                memory[mem] = cmd["value"]
    return memory


if __name__ == '__main__':
    script = read_input()
    MEMORY = execute(script)
    print(f"Sum of values in memory {sum(MEMORY.values())}")

    MEMORY2 = execute_v2(script)
    print(f"Sum of values in memory with v2 {sum(MEMORY2.values())}")
