class MedicalVisit:
    '''
    Model which stores a medical visit record. A medical visit is an instance
    where a patient consulted a doctor for any reason.

    patient(User) - Patient that attended this vist
    doctor(Doctor) - Doctor that attended to this visit
    '''
    def __init__(self, visitId=None, patient=None, doctor=None):
        if (visitId == None):
            print("Create self from random values")
        elif(patient == None or doctor == None):
            print("Get visit from database or cache")
            self.id = visitId
        else:
            self.id = visitId
            self.patient = patient
            self.doctor = doctor

