# we need a generator for geo locations

def locationGen():
    '''yield city-country pairs'''
    locations = [ # we might retrieve these from an API or DB
        ('Athlone','ie'),
        ('Galway','ie'),
        ('Hull','uk'),
        ('Canberra','aus'),
        ('Berlin','de'),
        ('Budapest', 'hu'),
        ('Madrid','es')
    ]
    index = 0
    while index < len(locations):
        # instead of return we use yield
        yield locations[index]
        index += 1

if __name__ == '__main__':
    inst = locationGen() # we have an instance of our generator
    print(inst.__next__()) # ('Athlone','ie')
    print(inst.__next__()) # ('Galway','ie')
    print(inst.__next__())
    # we can use a comprehension
    print([loc for loc in inst])