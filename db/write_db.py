'''write a single entry to our database'''

import sqlite3

def writeDB():
    '''populate the DB with one animal'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # sql statement (use double quotes)
    st = '''
    INSERT INTO zoo
    VALUES ("Penguin", 16, 0.52)
    '''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    writeDB()