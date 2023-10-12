from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def connect():
    """ Connect to MySQL database """
    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')

    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed.')


def query_with_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        # cursor.execute("SELECT * FROM students")
        # cursor.execute("SELECT * FROM scores")
        # cursor.execute("SELECT * FROM universities")
        cursor.execute("SELECT * FROM countries")

        # List of Queries
        query1(cursor)
        query2(cursor)
        query3(cursor)
        query4(cursor)
        query5(cursor)
        query6(cursor)
        query7(cursor)
        query8(cursor)
        query9(cursor)
        query10(cursor)

        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def query1(cursor):

def query2(cursor):

def query3(cursor):

def query4(cursor):

def query5(cursor):

def query6(cursor):

def query7(cursor):

def query8(cursor):

def query9(cursor):

def query10(cursor):



if __name__ == '__main__':
    connect()
    # query_with_fetchall()
