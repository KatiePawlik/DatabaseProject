from .populationData.populationDataUtils import getRandomName


class Doctor:
    randomId = 0

    def __init__(self, staffId=None, name=None):
        if (staffId == None):
            # "Create self from random values"
            self.id = Doctor.randomId
            Doctor.randomId += 1
            self.name = "Dr. {0}".format(getRandomName())
        elif (name == None):
            self.id = staffId
            # Get rest of doctor from database or cache or something
        else:
            self.id = staffId
            self.name = name

        # We probably aren't going to do anything with passwords so just leave them all the same
        self.password_hash = "#you've_been_hashed"
