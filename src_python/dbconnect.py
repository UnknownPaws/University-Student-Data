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
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    connect()
    # query_with_fetchall()
