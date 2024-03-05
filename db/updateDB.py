import sqlite3

def customUpdadte(w): # w will be an instance of a creature
    ''' update the count based on 'w' to alter the database'''
    q = int(float(w['count'])) # make sure it is an integer
    a = w['creature'] # which creature
    # we could also deal with the cost...
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # we can inject values into our SQL statement
    st = f'''
    UPDATE zoo
    SET count={q}
    WHERE creature = "{a}"
    '''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    # we need to specify which creature will be updated
    creature = {'creature':'Penguin', 'count':305, 'cost':432}
    customUpdadte(creature)
