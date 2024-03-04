# we can encapsulate data about a shape within a class
# this also allows us to validate the members of the class

# in Python everything is an object (even modules)
class Figure:
    '''It is common practice to document with triple quotes
    This allows new lines
    Figure class will capture sides, size and colour of a shape'''
    # NB every function within a class MUST receive 'self'
    def __init__(self, num_sides, size, colour='grey'): # like a constructor
        self.sides = num_sides # set some properties of this class
        self.size  = size
    # write methods to get and set the properties (inc validation)
    def set_num_sides(self, new_num_sides):
        if type(new_num_sides)==int or type(new_num_sides)==float:
            self.sides = new_num_sides
        else:
            raise TypeError # we could handle this problem
    # we can override built in features of Python
    def __str__(self):
        '''the __str__ method will be used whenever this class is printed'''
        return f'The figure has {self.sides} and size is {self.size}'

# usually in Python we use the following structure:
if __name__ == '__main__':
    fig1 = Figure(3, 6) # we now have an instance of our class
    # the print method always calls '__str__'
    print(fig1)
    fig1.set_num_sides('seven') # oh dear...
    print(fig1)