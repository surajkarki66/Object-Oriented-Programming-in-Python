""" Java Script Object Notation """

# There is two objects in this json file

import json


people_string = """

{

    "people": [
     {
         "name": "Suraj Karki",
         "phone": "9807111049",
         "emails": "suraj.karki500@gmail.com",
         "has_license": false


     },

     {

         "name": "Prakash Karki",
         "phone": "9807111049",
         "emails": "prakash.karki500@gmail.com",
         "has_license": true
     }



    ]
}
"""

# to convert it into python object called dictionary


print(type(people_string))

data = json.loads(people_string)

print(data)

print(type(data))

print("" * 5)


# to print each people
for people in data['people']:
    print(people)
    print(people['name'])
    print(people['emails'])


# to remove phone number from python object and convert it into json string

for people in data['people']:
    del people['phone']

new_string = json.dumps(data,indent=6,sort_keys=True)
print(new_string)