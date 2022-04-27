from cgitb import small


large = None
smallest = None

while True:
    num = input("Enter some number :")

    if num == "done":
        break

    if len(num) < 1:
        break

    try:
        num = float(num)
    except ValueError:
        print("Invalid input")
        continue

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

    if large is None:
        large = num
    elif num > large:
        large = num

print(f"Small is {smallest}")
print(f"Bigger is {large}")
