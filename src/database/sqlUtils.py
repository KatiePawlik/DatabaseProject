import sqlite3
from sqlite3 import Error
from utils.fileUtils import getDatabasePath



class sqlUtils():
    def __init__(self):
        print("hi")

    def addUserToDB(self, user):
        name = user.name
        identifier = user.id
        password = user.password_hash
        # C:/git/Git-Practice/DatabaseProject/PawlikLabs.db
        self.database = getDatabasePath()
        self.conn = None
        self.user = [(identifier, name, password), ]
        try:
            self.conn = sqlite3.connect(self.database)
            self.sql = '''INSERT INTO users(id, name, password_hash) VALUES(?,?,?)'''
            self.cur = self.conn.cursor()
            self.cur.executemany(self.sql, self.user)
            self.conn.commit()
            self.conn.close()
            # self.cur.close()

        except Error as e:
            # enable for debugging:
            print(e)
            return False

        return self.cur.lastrowid

    def addMedReportToDB(self, med_report):
        reportData = med_report.data
        identifier = med_report.id
        visitId = med_report.visit.id

        self.database = r"C:/git/Git-Practice/DatabaseProject/PawlikLabs.db"
        self.conn = None
        self.med_report = [(identifier, reportData, visitId), ]
        try:
            self.conn = sqlite3.connect(self.database)
            self.sql = '''INSERT INTO med_report(id, report_data, visit_id) VALUES(?,?,?)'''
            self.cur = self.conn.cursor()
            self.cur.executemany(self.sql, self.med_report)
            self.conn.commit()
            self.conn.close()
            # self.cur.close()

        except Error as e:
            # enable for debugging:
            print(e)
            return False

        return self.cur.lastrowid

    def addDoctorToDB(self, staff):
        self.name = staff.name
        self.identifier = staff.id
        self.password = staff.password_hash

        self.database = r"C:/git/Git-Practice/DatabaseProject/PawlikLabs.db"
        self.conn = None
        self.staff = [(self.identifier, self.name, self.password), ]
        try:
            self.conn = sqlite3.connect(self.database)
            self.sql = '''INSERT INTO staff(id, name, password_hash) VALUES(?,?,?)'''
            self.cur = self.conn.cursor()
            self.cur.executemany(self.sql, self.staff)
            self.conn.commit()
            self.conn.close()
            # self.cur.close()

        except Error as e:
            # enable for debugging:
            print(e)
            return False

        return self.cur.lastrowid

    def addVisitToDB(self, visit):
        self.patient = visit.patient
        self.notes = visit.notes
        self.identifier = visit.id
        self.doctor = visit.doctor

        self.database = r"C:/git/Git-Practice/DatabaseProject/PawlikLabs.db"
        self.conn = None
        self.visit = [(self.identifier, self.notes,
                       self.patient, self.doctor), ]
        try:
            self.conn = sqlite3.connect(self.database)
            self.sql = '''INSERT INTO med_visit(id, notes, patient, doctor) VALUES(?,?,?)'''
            self.cur = self.conn.cursor()
            self.cur.executemany(self.sql, self.visit)
            self.conn.commit()
            self.conn.close()
            # self.cur.close()

        except Error as e:
            # enable for debugging:
            print(e)
            return False

        return self.cur.lastrowid
