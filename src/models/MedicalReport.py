class MedicalReport:
    randomId = 0
    '''
    Medical Report model contains data from scans and additional tests which were
    run for a specific visit

    visit(MedicalVisit): Which visit was this report run for. This can be used to
    derive patient identification data
    
    init(None,None,visit)       - Create object from random values
    init(reportId, None, None)  - Create object with database lookup
    init(reportId, data, visit) - Create object from values
    '''

    def __init__(self, reportId=None, data=None, visit=None):
        if (reportId == None):
            # "Create self from random values
            self.id = MedicalReport.randomId
            MedicalReport.randomId += 1
            self.data = "Report data is here. Lab results or something."
            self.visit = visit
        elif (data == None or visit == None):
            self.id = reportId
            # Get report info from database or cache
        else:
            self.id = reportId
            self.data = data
            self.visit = visit
