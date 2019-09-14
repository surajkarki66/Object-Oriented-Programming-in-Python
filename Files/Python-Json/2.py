# JSON -> Java Script Object Notation

import json

# some json

x = '{"name":"Suraj","language":"Python"}'

# Parse x(.loads() load the json string)

y = json.loads(x)


# The result is python dictionary

print(y['name'])