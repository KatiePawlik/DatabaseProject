class Doctor:
    def __init__(self, staffId, name=None):
        if (staffId == None):
            print("Create self from random values")
        elif(name == None):
            self.id = staffId
            print("Get rest of doctor from database or cache or something")
        else:
            self.id = staffId
            self.name = name

        # We probably aren't going to do anything with passwords so just leave them all the same
        self.password_hash = "#you've_been_hashed"
