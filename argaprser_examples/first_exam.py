import argparse

parser = argparse.ArgumentParser(
    description="It is a parser argument"
)
tank_to_fish = {
    "tank_a": "shark, tuna, herring",
    "tank_b": "cod, flounder",
}

parser.add_argument("tank", type=str)
parser.add_argument("--upper-case", default=False, action="store_true", help="Transform text to upper case")

args = parser.parse_args()

fish = tank_to_fish.get(args.tank, "")

if args.upper_case:
    fish = fish.upper()

print(fish)
