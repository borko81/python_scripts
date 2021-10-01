import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("echo", type=str, help="Echo pararam...")
parser.add_argument(
    "--verbosity", "-v",
    help="Verbosity command",
    action="store_true"
)

args = parser.parse_args()

if args.verbosity:
    print("Verbosity is turned on")


print(args.echo * 2)
