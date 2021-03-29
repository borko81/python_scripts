base_10 = 231
# Octal
print(f"{base_10 :o}")

# hex with lowercase
print(f"{base_10 :x}")

#hex with uppercase
print(f"{base_10 :X}")

# Convert str to int
print(int('E7', base=16))

red = 12
green = 205
blue = 81

print(f"{red :02x}")
print(f"{green :02x}")
print(f"{blue :02x}")

rgb = (12, 205, 81)
print([f"{c :02x}" for c in rgb])