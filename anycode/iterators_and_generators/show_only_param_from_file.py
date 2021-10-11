FILE_NAME = r'C:\Program Files\Firebird\Firebird_2_5\firebird.conf'
result = []

with open(FILE_NAME) as f:
    while True:
        try:
            line = next(f)
            if line.startswith('#'):
                continue
            else:
                if line.strip():
                    print(line, end='')
        except StopIteration:
            break

# [print(line) for line in result if line.strip()]