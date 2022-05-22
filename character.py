import requests


class Character:
    def __init__(self, **kwargs):
        self.characterName = kwargs["characterName"]
        self.level = kwargs["level"]
        self.charClass = kwargs["charClass"]
        self.subclass = kwargs["subclass"]
        self.armorClass = kwargs["armorClass"]
        self.maxHP = kwargs["maxHP"]
        self.initiative = 0

    def rollInitiative(self):
        response = requests.get('https://cs361-numgen.herokuapp.com/?lower=1&upper=20')
        self.initiative = response.json()["randNum"]
