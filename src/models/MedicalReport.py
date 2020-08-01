class MedicalReport:
    '''
    Medical Report model contains data from scans and additional tests which were
    run for a specific visit

    visit(MedicalVisit): Which visit was this report run for. This can be used to
    derive patient identification data
    '''
    def __init__(self, reportId=None, data=None, visit=None):
        if (reportId == None):
            print("Create self from random values")
        elif(data == None or visit == None):
            self.id = reportId
            print("Get report info from database or cache")
        else:
            self.id = reportId
            self.data = data
            self.visit = visit