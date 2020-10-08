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
    with connection.cursor() as cursor:
        list_of_names = ['Fred', 'Bob']
        # prepare string form dynamic place holders
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name IN ({});".format(format_strings), list_of_names)
        connection.commit()
      

finally:
    # Close the connection, regardless of whether or not it was successful
    connection.close()
