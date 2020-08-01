class MedicalVisit:
    randomId = 0
    '''
    Model which stores a medical visit record. A medical visit is an instance
    where a patient consulted a doctor for any reason.

    patient(User) - Patient that attended this vist
    doctor(Doctor) - Doctor that attended to this visit
    
    init(None,patient,doctor)       - Create object from random values
    init(visitId, None, None)       - Create object with database lookup
    init(visitId, patient, doctor)  - Create object from values
    '''

    def __init__(self, visitId=None, patient=None, doctor=None):
        if (visitId == None):
            # "Create self from random values
            self.visitId = MedicalVisit.randomId
            MedicalVisit.randomId += 1
            self.patient = patient
            self.doctor = doctor

        elif (patient == None or doctor == None):
            # Get visit from database or cache
            self.id = visitId
        else:
            self.id = visitId
            self.patient = patient
            self.doctor = doctor
