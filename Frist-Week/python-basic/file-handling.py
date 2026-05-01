# File Handling Example

# Writing to file
with open("sample.txt", "w") as f:
    f.write("Hello, this is file handling example.\n")

# Appending to file
with open("sample.txt", "a") as f:
    f.write("Adding another line.\n")

# Reading file
with open("sample.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)