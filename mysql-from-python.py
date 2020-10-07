import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('root')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        rows = [("Joanna", 54, "1966-03-20 12:10:56"),
                ("Fred", 85, "1947-08-25 15:36:38"),
                ("Bob", 40, "1980-03-06 14:36:58")]
        cursor.executemany("INSERT INTO friends VALUES (%s, %s, %s);", rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether or not it was successful
    connection.close()
