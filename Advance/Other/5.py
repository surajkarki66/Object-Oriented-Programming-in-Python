# namedtuple
# you can put name in tuple elements
from collections import namedtuple



Lang = namedtuple('Lang',['language','rating'])

lang = Lang('python',8)

print(lang.language)
print(lang.rating)