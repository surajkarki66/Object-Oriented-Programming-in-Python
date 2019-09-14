import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# A simple serialization

data = {

    "Python":
       { "founder":"Guido Vann Russom",
         "type": "dynamically",
         "framework" : "django"
        }
}

print(data)

with open("prolang.json","w") as json_file:
    json.dump(data,json_file)

