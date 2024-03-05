'''Create (or open) a database'''
import sqlite3 # this database comes with Python

def accessDB():
    '''create a database and make a table for zoo animals
    Each creature wil have a count and a cost'''
    # we need a database access object
    conn = sqlite3.connect('my_db') # either create or open the database
    curs = conn.cursor() # this lets us work with the database
    # we need an SQL statement (by convention SQL keywords are in CAPITALS)
    st = '''
    CREATE TABLE zoo
    (
        creature VARCHAR(32) PRIMARY KEY,
        count int,
        cost float
    )
    '''
    try:
        curs.execute(st) # use the cursor to send the SQL statement to the DB
        conn.commit() # if all worked out fine, commit the changes
        conn.close() # always good to tidy up
    except Exception as err:
        print(err)

if __name__ == '__main__':
    accessDB()

# some other DB conn mechanisms
# see https://wiki.python.org/moin/DatabaseInterfaces
# DB2
# import DB2 # remember to pip install first!!
# conn = DB2.connect(dsn='ibm-DB', uid='analyst', pwd='db2pwd')

# Sybase
# import Sybase
# conn = Sybase.connect('SYBASE', 'username', 'passwd', 'databasename')

# Oracle
# import cx_Oracle
# conn = cx_Oracle.connect('username', 'passwd', 'hostname:port/SID')
# conn2 = cx_Oracle.connect('username/passwd@hostname:portno/SID')
# dsn_tns = cx_Oracle.makedsn('hostname', portno, 'SID')
# conn3 = cx_Oracle.connect('username', 'passwd', dsn_tns)

# MySQL
# import MySQLdb
# conn = MySQLdb.connect(host = "hostname", user = "username", passwd = "password", db = "dbname")

# PySQLite
# from pysqlite2 import dbapi2 as sqlite
# conn = sqlite.connect("mydb", connectionproperties)

# ODBC
# import odbc
# conn = odbc. odbc("myDSN/username/password")