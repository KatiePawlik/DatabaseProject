from .populationData.populationDataUtils import getRandomName


class User:
    randomId = 0

    def __init__(self, userId=None, name=None):
        if (userId == None):
            # "Create self from random values"
            self.id = User.randomId
            User.randomId += 1
            self.name = getRandomName()
        elif (name == None):
            # "Get rest of values from DB or cache"
            self.id = userId
        else:
            self.id = userId
            self.name = name

        # We probably aren't going to do anything with passwords so just leave them all the same
        self.password_hash = "#you've_been_hashed"
