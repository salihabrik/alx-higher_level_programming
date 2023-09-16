#!/usr/bin/python3
"""
Module that connects a python script to a database
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    # Connect database
    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)
    # Create cursor obj to interact with database
    my_cursor = my_db.cursor()

    # Execute a SELECT query
    my_cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

    # fetch all the data returned
    my_data = my_cursor.fetchall()
    for row in my_data:
        print(row)

    # Close all cursors
    my_cursor.close()

    # Close all databasess
    my_db.close()
