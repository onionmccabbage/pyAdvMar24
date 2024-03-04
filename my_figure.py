# we can encapsulate data about a shape within a class
# this also allows us to validate the members of the class

# in Python everything is an object (even modules)
class Figure: # by default we inherit from 'object' like Figure(object)
    '''It is common practice to document with triple quotes
    This allows new lines
    Figure class will capture sides, size and colour of a shape'''
    # NB every function within a class MUST receive 'self'
    def __init__(self, num_sides, size, colour='grey'): # like a constructor
        self.sides = num_sides # set some properties of this class
        self.size  = size # self.size will call the setter method
    # write methods to get and set the properties (inc validation)
    @property # we declare this method to behave as a property
    def size(self): # here is the 'getter' method for 'size'
        return self.__size
    @size.setter
    def size(self, new_size): # here is the 'setter' method for size
        if type(new_size) in (int, float):
            self.__size = new_size # double-underscore is called 'name mangling'
        else:
            self.__size = 4 # a sensible default

    def set_num_sides(self, new_num_sides):
        if type(new_num_sides)==int or type(new_num_sides)==float:
            self.sides = new_num_sides
        else:
            raise TypeError # we could handle this problem
    # we can override built in features of Python
    def __str__(self):
        '''the __str__ method will be used whenever this class is printed'''
        return f'The figure has {self.sides} and size is {self.size}' # access the size getter

# usually in Python we use the following structure:
if __name__ == '__main__':
    fig1 = Figure(3, 6) # we now have an instance of our class
    fig2 = Figure(3, 6) 
    # compare instances
    print(fig1, fig2, fig1==fig2) # fig1 and fig2 are in different memory so they are NOT the same
    # the print method always calls '__str__'
    print(fig1)
    fig1.set_num_sides(7) # all good
    fig1.size = 8 # this will call the size setter method
    fig1.size = 'oops' # this will set the default 4
    print(fig1)
