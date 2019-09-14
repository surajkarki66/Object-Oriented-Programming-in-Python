with open("friends.txt","r") as file:


    f = file.readlines()

    friends_list = [line.strip() for line in f]   # Remove all hidden characters like \n,\t

input_friends = input("Enter the friends name").split(",")



friends_list_set = set(friends_list)

input_friends_set = set(input_friends)


common = friends_list_set.intersection(input_friends_set)

common_str = list(common)
print(common_str)

for n in common_str:
    with open('matching.txt','w') as file1:
        file1.write(n)
    


