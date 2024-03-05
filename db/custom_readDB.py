import sqlite3

def customRead(w):
    '''read specific members from teh zoo table in the DB'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # we can use string formatting to iject values into an SWL statement
    st = f'''
    SELECT creature, count, cost FROM zoo
    WHERE creature = "{w}"
    '''
    try:
        curs.execute(st)
        conn.commit()
        rows = curs.fetchall()
        conn.close
    except Exception as err:
        print(err)
    return rows

if __name__ == '__main__':
    w = input('Which creature? ')
    r = customRead(w)
    # iterate over all results
    for animal in r:
        print(f'We have {animal[1]} {animal[0]} costing {animal[2]}')
