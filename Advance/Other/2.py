# default arguments

currency = {
    'Us': 100,
    'Uk': 150,
    'Aus':90
}

def update(value,name='Aus'):
    currency[name] += value
    return currency[name]

update(10)

print(currency['Aus'])


#Argument unpacking

curencies = [
    ('Us',100),
    ('Uk',-19),
    ('Aus',34)
]

for c in curencies:
    update(name=c[0],value=c[1])
print(currency)

# queues-> add from one end and remove from other end

