from io import StringIO
import io

text = "Some unusefull text is here"

temp_file = StringIO(text)

# print(temp_file.read())
temp_file.seek(0, io.SEEK_END)
temp_file.write("End")
temp_file.seek(0)
print(temp_file.read())
