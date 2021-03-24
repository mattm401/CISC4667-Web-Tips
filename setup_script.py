"""
setup_script.py
This script is designed to provide an example of creating and inserting into a sqlite database.
"""

import sqlite3
from sqlite3 import Error


def create_table(conn, create_table_sql):
    """
    create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)

    except Error as e:
        print('Error: ' + str(e))


def insert_log_message(name, statement):
    """
    insert a record into the specified table
    :param name: provide the name of the existing database
    :param statement: provide a valid insert statement
    """
    try:
        conn = sqlite3.connect(name + '.db')
        if conn:
            c = conn.cursor()
            c.execute('INSERT INTO Log (log_message) VALUES (?)', statement)
            conn.commit()
    except Error as e:
        print('Error: ' + str(e))
    finally:
        if conn:
            conn.close()


def create_database(name):
    """
    create a connection and a table if one doesn't exist
    :param name: provide a name for the database
    """
    conn = None
    sql_create_sample_table = 'CREATE TABLE IF NOT EXISTS Log (log_id INTEGER PRIMARY KEY AUTOINCREMENT, log_message ' \
                              'VARCHAR(255) NOT NULL);'

    try:
        conn = sqlite3.connect(name + '.db')
        if conn:
            create_table(conn, sql_create_sample_table)
    except Error as e:
        print('Error: ' + str(e))
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_database('sample')
    insert_log_message('sample', ['A message to test the log table'])
    print('Script executed.')

