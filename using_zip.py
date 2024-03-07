# zip in Python has nothing to do with compression archives etc.

def main():
    '''we can use zip to combine separate data structures'''
    days_l   = ['Mon', 'Tues', 'Weds', 'Thur']
    fruit_t  = ('Banana', 'Orange', 'Kiwi', 'Durian')
    drinks_s = {'Coffee', 'Tea', 'Water', 'Calpico'}
    afters_t = ('Tiramisu', 'Crumble', 'Crepe')
    # zip will only use the number of members in the shortest collection
    z = zip(days_l, fruit_t, drinks_s, afters_t)
    print(z, type(z))
    for day, fruit, drink, pud in z:
        print(f'On {day} we offer {fruit} with {drink} then {pud}')

if __name__ == '__main__':
    main()