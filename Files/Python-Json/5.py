import json

with open('states.json') as f:
    # To convert into python file object
    data = json.load(f)


for state in data['states']:
   # print(state)
    print(state['name'],state['abbreviation'])


# lets delete the area code from object

for state in data['states']:
    del state['area_codes']
    
with open('new_states.json','w') as f:
    json.dump(data,f,indent=2) 