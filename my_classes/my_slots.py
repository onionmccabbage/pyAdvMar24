# slots allow us to restrict the members of a class
class Restricted():
    __slots__ = ('x', 'y') # a tuple of permitted properties
    def __init__(self, x,y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    r = Restricted(4,3)
    r.z = 5  # should fail - there is no slot for z