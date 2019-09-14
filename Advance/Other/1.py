"Argument Mutability"

friends_last_seen = {
    'Rojan':22,
    'Binish':24,
    'Suraj':39,
    'Saman':31
}

def see_friends(friends,name):
 #   print(id(friends))
    friends[name] = 0
    print(friends['Rojan'])
    print(friends['Binish'])

#print(id(friends_last_seen))
see_friends(friends_last_seen,'Rojan')
#print(id(friends_last_seen))

print(friends_last_seen['Rojan'])    # The value of rojan is also change outside the function



age = 10

def increase_age(current):
    current += 1

print(age)
increase_age(age)
print(age)


primes = [1,3,5]
print(id(primes))

print(primes)

#primes += [7,9]  # primes = primes.__iadd__()
primes = primes + [7,9]   # primes = primes.__add__()

print(primes)

print(id(primes))


