file_name = "example_demo.txt"

with open(file_name, "r") as f:
    print(f.read())

with open(file_name, "w") as f:
    f.write("Welcome to the file")


with open(file_name, "r") as f:
    print(f.read())
