import sqlite3

def populateCreatues(creatures_t):
    '''iterate over every member of the tuple, writing each to the DB'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # we can write robust SQL using wildcards '?' for inserted values
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    for item in creatures_t:
        try:
            if type(item['creature']==str):
                n = item['creature']
            else:
                raise Exception('Creature name must be a string')
            if type(item['count']==int):
                count = item['count']
            else:
                raise Exception('Creature count must be an integer')
            if type(item['cost']) in (int, float):
                cost = item['cost']
            else:
                raise Exception('Creatue cost must be int or float')
            # if everything is ok, we can commit to the DB
            curs.execute(st, (n, count, cost)) # pass a tuple to replace the widlcards
            conn.commit()
        except Exception as err:
            print(err)
    conn.close() # when we are done, close the connection


if __name__ == '__main__':
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    ) 
    populateCreatues(creatures_t)