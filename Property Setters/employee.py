class Employee:
    def __init__(self,first,last,tag):
        self.first = first
        self.last = last
        self.tag = tag
    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @email.setter
    def email(self,name):
        first,last = name.split('.')
        self.first = first
        self.last = last
    
        

    
e = Employee('suraj','karki','email')

print(e.email)

e.email = 'michael.karki'

print(e.email)

    