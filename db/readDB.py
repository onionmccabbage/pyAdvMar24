import sqlite3

def readDB():
    '''read back from the database'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # we can SELECT * to get everything
    # often it is preferable to choose the order of which columns we need
    st = '''
    SELECT creature, count, cost FROM zoo
    '''
    try:
        curs.execute(st)
        conn.commit()
        # we can now access the results of our SQL statement
        rows = curs.fetchall() # grab every result from the executed SQL statement
        return rows
    except Exception as err:
        print(err)

if __name__ == '__main__':
    c = readDB() # try to read all the rows from the zoo table in our DB
    for animal in c:
        print(f'we have {animal[1]} {animal[0]} each costing {animal[2]}')