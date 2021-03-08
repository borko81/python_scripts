import sys
import os

# Platform
print(sys.platform)
# Version
print(sys.version)

if sys.platform[:3] == 'win':
    print("Use Windows")

# Path
sys.path.insert(0, os.getcwd())
print(sys.path)

# Print directory in windwos without use slash
print(os.path.exists(r'C:'))

print(sys.modules.keys())

# Raise errors
try:
    raise IndexError
except IndexError:
    print(sys.exc_info())