import sqlite3
from sqlite3 import Error

class sqlUtils():
    def __init__(self):
        print("hi")
    def addRowtoTable(self, identifier, name, password):
        self.database = r"C:/git/Git-Practice/DatabaseProject/PawlikLabs.db"
        self.conn = None
        self.user = [(identifier, name, password),]   
        try:
            self.conn = sqlite3.connect(self.database)
            self.sql = '''INSERT INTO users(id, name, password_hash) VALUES(?,?,?)'''
            self.cur = self.conn.cursor()
            self.cur.executemany(self.sql, self.user)
            self.conn.commit()

        except Error as e: 
            # enable for debugging:
            # print(e)
            return False
        
        return self.cur.lastrowid
