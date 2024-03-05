'''Python uses == to compare objects for equality'''
# There are many built-in features of Python which we can override
# e.g. __str__, __exit__ NB they all have leading and trailing dunder (double underscore)
# For equality, the built in is called __eq__

class Word():
    '''this class overrides the equality operator to ignore case'''
    def __init__(self, text):
        self.text = text # we could use property get/set
    def __eq__(self, other):
        '''in place of the default == this class will use our __eq__ function'''
        answer = self.text.lower() == other.text.lower()
        return answer

if __name__ == '__main__':
    word1 = 'Hello'
    word2 = 'hello'
    print(word1 == word2)
    # try our class
    w1 = Word('hello')
    w2 = Word('Hello')
    print(w1 == w2) # True

# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# other 'magic methods'
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object