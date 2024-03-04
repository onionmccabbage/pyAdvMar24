from my_abstract import AbstractShape

# here is a concrete class
class Shape(AbstractShape):
    def __init__(self, name):
        self.shape_name = name
    
    # getter and setters
    @property
    def shape_name(self):
        return self.__shape_name
    @shape_name.setter
    def shape_name(self, new_name):
        if type(new_name)==str and new_name !='':
            self.__shape_name = new_name
        else:
            raise TypeError('shape name must be a non-empty string')
    def __str__(self):
        return f'This shape is called {self.shape_name}'
    
if __name__ == '__main__':
    try:
        sq = Shape('square')
        pe = Shape('Pentagon')
        print(sq, pe)
        # check the TypeError is raised
        oops = Shape('') # raise a TypeError
    # handle specific exceptions first
    except TypeError as err:
        print(f'There is a problem: {err}')
    # handle more generic exceptions
    except Exception as err:
        print(f'An unknown exception happened: {err}')
    finally:
        # always runs, even if there is an exception
        print('finally block...')
    # unless we use slots, we can add any arbitrary property
    sq.ooblywoob = 'lunchtime'
    print(sq.ooblywoob)