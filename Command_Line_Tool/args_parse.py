import argparse


def check_name():
    parser = argparse.ArgumentParser(description="Test how work arparse")
    parser.add_argument("integers", type=int, nargs="+", help="Enter some argument")
    args = parser.parse_args()
    print(args.integers)


if __name__ == '__main__':
    check_name()
