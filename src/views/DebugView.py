from views.lib.Menu import Menu
from views.lib.Common import pause

from models.User import User
from models.Doctor import Doctor
from database.sqlUtils import sqlUtils
from models.MedicalReport import MedicalReport
from models.MedicalVisit import MedicalVisit

class DebugView:
    def __init__(self):
        pass

    def render(self):
        options = ["Run test code 1", "Run test code 2", "Back"]
        menu = Menu(options)
        selection = menu.render()
        if (selection == 0):
            sqlManager = sqlUtils()

            testUser = User(10, "Billy Joel")
            testDoctor = Doctor(10, "Katie Pawlik")
            visit = MedicalVisit(10, testUser, testDoctor)
            medicalReport = MedicalReport(10, "X-Ray that says no fungus", visit)

            sqlManager.addUserToDB(testUser)
            print("Finished")
            pause()
            # sqlManager.addMedReportToDB(medicalReport)
        elif (selection == 1):
            print(1)
        elif (selection == 2):
            return 0

        self.render()
