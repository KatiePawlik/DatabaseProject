class User:
    def __init__(self, userId=None, name=None):
        if(userId == None):
            print("Create self from random values")
        elif(name == None):
            print("Get rest of values from DB or cache")
            self.id = userId
        else:
            self.id = userId
            self.name = name

        # We probably aren't going to do anything with passwords so just leave them all the same
        self.password_hash = "#you've_been_hashed"
