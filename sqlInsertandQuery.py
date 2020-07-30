import sqlite3
from sqlite3 import Error

def connectionSetUp(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e: 
        print(e)

    return connection

def Table1SetUp(connection, project):
    sql = '''INSERT INTO _____()
        VALUES(?,?,?)'''
    cursor = connection.cursor()
    cursor.execute(sql, project)
    connection.commit()
    return cursor.lastrowid

def main():
    database = r"filepath"
    connection = connectionSetUp(database)
    with connection:
        project = ('data', 'data', 'data')
        project_id = Table1SetUp(connection, project)

if __name__ == "__main__":
    main()