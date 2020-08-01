'''
1. Create users
2. Create doctors
3. Create visits
4. Create reports

Append to file
5. Insert users
6. Insert doctors
7. Insert visits
6. Insert reports

Execute script
'''
import random

from models.Doctor import Doctor
from models.User import User
from models.MedicalReport import MedicalReport
from models.MedicalVisit import MedicalVisit
from database.sqlUtils import sqlUtils


def getRandomUsers(amount):
    users = []
    for i in range(amount):
        users.append(User())
    return users


def getRandomDoctors(amount):
    doctors = []
    for i in range(amount):
        doctors.append(Doctor())
    return doctors


def getRandomMedicalVisits(amount, userPool, doctorPool):
    medicalVisits = []
    for i in range(amount):
        repeatVisitCount = random.randint(1, 6)
        doctor = doctorPool[random.randint(0, len(doctorPool) - 1)]
        patient = userPool[random.randint(0, len(userPool) - 1)]
        for i in range(repeatVisitCount):
            medicalVisits.append(MedicalVisit(None, patient, doctor))
    return medicalVisits


def getRandomMedicalReports(amount, visitPool):
    reports = []
    for i in range(amount):
        sameVistReportCount = random.randint(0, 3)
        visit = visitPool[random.randint(0, len(visitPool) - 1)]
        for i in range(sameVistReportCount):
            reports.append(MedicalReport(None, visit))
    return reports


def populateDataBase(amount):
    users = getRandomUsers(amount)
    doctors = getRandomDoctors(amount)
    visits = getRandomMedicalVisits(amount, users, doctors)
    reports = getRandomMedicalReports(amount, visits)

    sqlUtil = sqlUtils()
    for user in users:
        sqlUtil.addUserToDB(user)
