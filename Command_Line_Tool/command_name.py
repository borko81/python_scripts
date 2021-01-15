tries = 0

while True:
    name = input("Enter your name: ")
    if name is not None and name != '':
        break
    else:
        tries += 1
    if tries >= 3:
        break
    else:
        continue

print(name)