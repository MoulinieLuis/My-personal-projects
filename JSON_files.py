import json

# Writing data to JSON
data = {"name": "Luis", "age": 25}
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading data from JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)
print(loaded_data)