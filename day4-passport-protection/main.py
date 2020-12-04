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


def validate_field(key, value):
    if key == "byr":
        return 1920 <= int(value) <= 2002
    if key == "iyr":
        return 2010 <= int(value) <= 2020
    if key == "eyr":
        return 2020 <= int(value) <= 2030
    if key == "hgt":
        if value.endswith("cm"):
            return 150 <= int(value[:-2]) <= 193
        elif value.endswith("in"):
            return 59 <= int(value[:-2]) <= 76
        else:
            raise Exception("Not good height")
    if key == "hcl":
        return bool(re.match("#[0-9a-f]{6}$", value))
    if key == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if key == "pid":
        return bool(re.match("[0-9]{9}$", value))
    if key == "cid":
        return True


def is_strictly_valid(passport):
    try:
        fields_valid = [validate_field(k, v) for k, v in passport.items()]
        return is_valid(passport) and all(fields_valid)
    except Exception:
        return False


def count_strictly_valid(passports):
    return [is_strictly_valid(passport) for passport in passports].count(True)


if __name__ == '__main__':
    passport_info = read_input()
    print(f"All passport info dicts: {passport_info}")
    print(f"Valid passports {count_valid(passport_info)}")
    print(f"Strictly valid passports {count_strictly_valid(passport_info)}")
