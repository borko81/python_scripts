import argparse

parser = argparse.ArgumentParser()

parser.add_argument("num1", type=int, help="First param")
parser.add_argument("num2", type=int, help="Second param")
parser.add_argument("--option", "-o", default="add", type=str, help="Calculate the result")


args = parser.parse_args()


data = {
    "add": lambda x, y: x + y,
    "multiply": lambda x, y: x * y
}


result = data[args.option](args.num1, args.num2)
print(result)
