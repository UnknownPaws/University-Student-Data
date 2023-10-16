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


def queries():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor(buffered=True)

        """Query"""
        print('Number of top 200 universities in the USA: ' + str(query1(cursor)),
              'Number of top 200 universities in the UK: ' + str(query2(cursor)),
              'Number of unique universities represented in the student score dataset: ' + str(query3(cursor)),
              'Average score (0-100) of Harvard students in the student score dataset: ' + str(query4(cursor, 'Harvard University')),
              'Country with the most efficient budgeting of money on higher education (calculated by multiplying teaching score by percent gdp spent of higher education): ' + query8(cursor),
              sep='\n')

        rows = cursor.fetchall()

        # print('Total Row(s):', cursor.rowcount)
        # for row in rows:
        #     print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def query1(cursor):
    cursor.execute('SELECT COUNT(*) FROM universities WHERE country = "United States of America";')
    return cursor.fetchone()[0]

def query2(cursor):
    cursor.execute('SELECT COUNT(*) FROM universities WHERE country = "United Kingdom";')
    return cursor.fetchone()[0]

def query3(cursor):
    cursor.execute('SELECT COUNT(DISTINCT UNIVERSITY) FROM students;')
    return cursor.fetchone()[0]

def query4(cursor, university_name):
    cursor.execute('SELECT generalManagementScore, domainSpecificScore FROM students INNER JOIN scores USING(id) WHERE university = "' + university_name + '";')
    all_scores = cursor.fetchall()
    total_score = 0

    for studentScores in all_scores:
        total_score += studentScores[0] + studentScores[1]

    if len(all_scores) > 0:
        return total_score/len(all_scores)
    return 0

# def query5(cursor):

# def query6(cursor):

# def query7(cursor):

def query8(cursor):
    cursor.execute('SELECT DISTINCT country FROM countries INNER JOIN universities USING(country) WHERE gdp_percent IS NOT NULL;')
    countries = cursor.fetchall()

    best_country = str()
    best_score = int()

    for country in countries:
        cursor.execute('SELECT teaching_score, gdp_percent FROM countries INNER JOIN universities USING(country) WHERE gdp_percent IS NOT NULL AND country = "' + country[0] + '";')
        score_and_gdp_table = cursor.fetchall()
        country_score = 0

        for score_and_gdp in score_and_gdp_table:
            teaching_score = score_and_gdp[0]
            gdp_percent = score_and_gdp[1]
            country_score += teaching_score * gdp_percent

        # score_and_gdp_table should never be 0 at this point
        country_score /= len(score_and_gdp_table)

        if country_score > best_score:
            best_score = country_score
            best_country = country[0]

    return best_country


# def query9(cursor):

# def query10(cursor):



if __name__ == '__main__':
    # connect()
    queries()
