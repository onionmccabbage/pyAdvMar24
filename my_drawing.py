# we can import the figure class
from my_figure import Figure

# this class will inherit from 'Figure'
class Drawing(Figure):
    '''We now have everything from the 'Figure' class
    In addition we declare a 'line_thickness' property'''
    def __init__(self, num_sides, size, colour='black', line_thickness=0.1):
        super().__init__(num_sides, size, colour) # call teh __init__ of the parent class
        self.line_thickness = line_thickness # we have name mangling,so we should declare a @property
    @property # this is the getter
    def line_thickness(self):
        return self.__line_thickness
    @line_thickness.setter
    def line_thickness(self, new_thickness):
        if type(new_thickness) in (int, float):
            self.__line_thickness = new_thickness
        else:
            pass # fail silently
    # we could write a new __str__ method too

if __name__ == '__main__':
    d1 = Drawing(7, 2, 'green', 0.2)
    d1.line_thickness = 0.05 # this will call the line_thickness setter method
    print(d1, d1.line_thickness) # this will call the line_thickness getter method