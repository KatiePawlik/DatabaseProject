import random
import json

NAME_FILE = 'models/populationData/girl_boy_names_2018.json'


def getRandomName():
    if (random.randint(0, 1) == 0):
        return getRandomBoyName()
    else:
        return getRandomGirlName()


def getRandomGirlName():
    with open(NAME_FILE, 'r') as file_content:
        content = file_content.read()
        data = json.loads(content)
        randIndex = random.randint(0, len(data['girls']))
        return data['girls'][randIndex]


def getRandomBoyName():
    with open(NAME_FILE, 'r') as file_content:
        content = file_content.read()
        data = json.loads(content)
        randIndex = random.randint(0, len(data['boys']))
        return data['boys'][randIndex]
