"""Day 4 advent of code 2020"""
import re

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def passport_dict(chunk):
    fields = chunk.replace("\n", " ").rstrip().split(" ")
    return {k: v for k, v in [field.split(":") for field in fields]}


def read_input():
    with open("input", "r") as input_file:
        data = input_file.read()
        return [passport_dict(chunk) for chunk in re.split("\n\n", data)]


def is_valid(passport):
    return REQUIRED_FIELDS.issubset(set(passport.keys()))


def count_valid(passports):
    return [is_valid(passport) for passport in passports].count(True)


if __name__ == '__main__':
    passport_info = read_input()
    print(f"All passport info dicts: {passport_info}")
    print(f"Valid passports {count_valid(passport_info)}")
