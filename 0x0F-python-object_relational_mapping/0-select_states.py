#!/usr/bin/python3
"""
Script to connect to a MySQL server and retrieve a list of states from the database.
"""

import MySQLdb
import sys


def select_states(username, password, database):
    """
    Connects to a MySQL server and retrieves a list of states from the specified database.

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

    # Execute SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    db.close()

    return rows


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py username password database")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Retrieve the list of states
    states = select_states(username, password, database)

    # Print the states in the specified format
    for state in states:
        print(state)
