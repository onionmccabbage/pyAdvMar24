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
            pass

    def __str__(self):
        return f'This shape is called {self.shape_name}'
    
if __name__ == '__main__':
    sq = Shape('square')
    pe = Shape('Pentagon')
    print(sq, pe)