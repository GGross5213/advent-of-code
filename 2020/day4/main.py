import re


class PassportAttributeCheck:
    def __init__(self, attr_type, data_check):
        self.attr_type = attr_type
        self.data_check = data_check

    def is_valid(self, attr):
        typed_attr = self.attr_type(attr)

        return self.data_check(typed_attr)


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

passport_attr_checks = {
    "byr": PassportAttributeCheck(
        int, lambda x: len(str(x)) == 4 and x >= 1920 and x <= 2002
    ),
    "iyr": PassportAttributeCheck(
        int, lambda x: len(str(x)) and x >= 2010 and x <= 2020
    ),
    "eyr": PassportAttributeCheck(
        int, lambda x: len(str(x)) and x >= 2020 and x <= 2030
    ),
    "hgt": PassportAttributeCheck(
        str,
        lambda x: re.match(r"\d{2,3}(cm|in)", x) is not None
        and (
            int(x.split("in")[0]) >= 59 and int(x.split("in")[0]) <= 76
            if "in" in x
            else True
        )
        and (
            int(x.split("cm")[0]) >= 150 and int(x.split("cm")[0]) <= 193
            if "cm" in x
            else True
        ),
    ),
    "hcl": PassportAttributeCheck(
        str, lambda x: re.match(r"^#[a-f0-9]{6}$", x) is not None
    ),
    "ecl": PassportAttributeCheck(
        str,
        lambda x: x
        in [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth",
        ],
    ),
    "pid": PassportAttributeCheck(
        str, lambda x: re.match(r"^[0-9]{9}$", x.strip()) is not None
    ),
}


def part1(input_data: str):
    valid_passports = 0

    for passport in input_data.split("\n\n"):
        valid_passports += int(
            all([a in passport for a in passport_attr_checks.keys()])
        )

    print(f"Part 1: {valid_passports}")


def part2(input_data):
    valid_passports = 0

    for passport in input_data.split("\n\n"):
        attributes = {
            attr.split(":")[0]: attr.split(":")[1]
            for attr in passport.replace("\n", " ").split(" ")
        }

        valid_passports += int(
            all([a in attributes for a in passport_attr_checks.keys()])
            and all(
                [
                    check.is_valid(attributes[attr])
                    for attr, check in passport_attr_checks.items()
                ]
            )
        )

    print(f"Part 2: {valid_passports}")


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_data = file.read()

    part1(input_data)
    part2(input_data)