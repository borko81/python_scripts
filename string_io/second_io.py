from io import StringIO

# Retrieve value

file = StringIO("This is my text")

# Getvalue not moove index to the end
print(file.getvalue())

# read moove index to the end
print(file.read())

# Not print anything
print(file.read())

# Moove cursor to the begin
file.seek(0)

print(file.read())

# Truncate file, remove everything after index in trunc
file.seek(0)
file.truncate(4)
print(file.read())
# Show current position of the cursor
print(file.tell())

# Finallt close the file
file.close()
# Return Error
print(file.read())
