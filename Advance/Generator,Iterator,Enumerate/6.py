# Filter
# Filter returns a generator

def starts_with_r(friends):
    return friends.startswith('R')

friends = ['Rupesh','Ruchi','Binish','Ram']

starts_with_r = filter(starts_with_r,friends)

#print(starts_with_r)

print(next(starts_with_r))
print(list(starts_with_r))


def my_custom_filter(func,iterable):
    for i in iterable:
        if func(i):
            yield i


my_custom_filter(starts_with_r,friends)

#print(next(starts_with_r))