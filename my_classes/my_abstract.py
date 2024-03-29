from abc import ABCMeta, abstractmethod # these are built in libraries in Python

# we may declare our own abstract class
class AbstractShape(metaclass=ABCMeta): # this is how we declare an Abstract Base Class
    def __init__(self):
        pass
    '''Abstraction means we can declare properties and methods we will need in concrete classes'''
    @abstractmethod
    def __str__(self):
        '''we will definitely need a __str__ method in our concrete class'''
    @abstractmethod
    def shape_name(self, new_name):
        pass # we do not declare any functionality in the abstract