# collections
# counter

from collections import Counter

friends  = [1,2,4,2,1,4,5,4,6,7]

friends_count = Counter(friends)

#print(friends_count.values())
print(friends_count[2])   # there 2 fours in the list

# We also use dictionary