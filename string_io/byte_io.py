import io

string = io.BytesIO(b"The name is excelent: \x00\x01")

print(string.getvalue())
