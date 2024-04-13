#!/usr/bin/python3
"""
Script to connect to a MySQL server and retrieve states
with names starting with 'N'
from the specified database.
"""

import MySQLdb
import sys


def filter_states(username, password, database):
    """
    Connects to a MySQL server and retrieves states with names
    starting with 'N'
    from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        list: List of tuples containing state IDs and names.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    db.close()

    return rows


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Retrieve the list of states starting with 'N'
    filtered_states = filter_states(username, password, database)

    # Print the filtered states in the specified format
    for state in filtered_states:
        print(state)
