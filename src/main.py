from models.User import User
from models.Doctor import Doctor
from database.sqlUtils import sqlUtils
from models.MedicalReport import MedicalReport
from models.MedicalVisit import MedicalVisit


sqlManager = sqlUtils()

testUser = User(10, "Billy Joel")
testDoctor = Doctor(10, "Katie Pawlik")
visit = MedicalVisit(10, testUser, testDoctor)
medicalReport = MedicalReport(10, "X-Ray that says no fungus", visit)

sqlManager.addUserToDB(testUser)

#sqlManager.addMedReportToDB(medicalReport)
