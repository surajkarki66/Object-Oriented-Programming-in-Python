# defaultdict
# it never raises a key error in dictionary
from collections import defaultdict

friends = [('Binish','CalTech'),('Saman','Harvard'),('Suraj','MIT')]

inDict = {}

for f in friends:
    if friends[0] is not inDict:
        inDict[friends[0]] = []
inDict[friends[0]].append(friends[1])

print(inDict)

Dict = {'name':'suraj','roll':12,'section':'A'}
Dict = defaultdict(dict)   # it always takes function
print(Dict['ram'])