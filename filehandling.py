import csv
import json

# with open("data.csv","r") as file:
#     read = csv.reader(file)
#     for row in read:
#         print(row)

data =  {
    "name":"Lucky",
    "designation":"Engineer"
}

with open("user.json","w") as file:
    json.dump(data,file)

with open("user.json","r") as file:
    content = json.load(file)
    print(type(content))