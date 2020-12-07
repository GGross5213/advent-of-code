from typing import Dict, List, Set, Tuple
from collections import defaultdict


def parse_rule(rule: str) -> Dict:
    outer_bag, inner_bags = [
        p.replace(".", "").replace("bags", "").replace("bag", "").strip()
        for p in rule.split("contain")
    ]

    inner_bag_lookup = {
        bag[2:]: int(bag[0])
        for bag in inner_bags.split(" , ")
        if bag.strip()[:2] != "no"
    }

    return {outer_bag: inner_bag_lookup}


def parse_rules_to_lookup(rules: List[str]) -> Tuple[Dict, Dict]:
    contains_lookup = {}
    containedin_lookup = defaultdict(set)

    for rule in rules:
        parsed_rule = parse_rule(rule)
        contains_lookup.update(parsed_rule)

        [
            containedin_lookup[inner_bag].add(outer_bag)
            for outer_bag, inner_bags in parsed_rule.items()
            for inner_bag in inner_bags.keys()
        ]

    return contains_lookup, containedin_lookup


def find_all_outer_bags(inner_bag: str, containedin_lookup: Dict, holds_bag: Set):
    for bag in containedin_lookup[inner_bag]:
        holds_bag.add(bag)
        find_all_outer_bags(bag, containedin_lookup, holds_bag)

    return holds_bag


def part_1(data: str):
    _, containedin_lookup = parse_rules_to_lookup(data.split("\n"))

    holds_bag = set()

    find_all_outer_bags("shiny gold", containedin_lookup, holds_bag)

    print("Part 1: ", len(holds_bag))


def count_inner_bags(outer_bag, contains_lookup):
    total = 0
    # if outer_bag not in contains_lookup:
    #     return total

    for bag, count in contains_lookup[outer_bag].items():
        total += count
        total += count * count_inner_bags(bag, contains_lookup)

    return total


def part_2(data: str):
    contains_lookup, _ = parse_rules_to_lookup(data.split("\n"))

    bag_count = count_inner_bags("shiny gold", contains_lookup)

    print("Part 2: ", bag_count)


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()