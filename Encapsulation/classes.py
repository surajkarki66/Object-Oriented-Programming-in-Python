# actually in python there is no convention of private and public classes
# But we use pseudo do mimic the private and public classes

class _Private:
    def __init__(self, name):
        self.name = name


class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def display(self):
        print("hello")
