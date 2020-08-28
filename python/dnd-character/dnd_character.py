class Character:
    def __init__(self):
        self.strength = self.calculateScores()
        self.dexterity = self.calculateScores()
        self.constitution = self.calculateScores()
        self.intelligence = self.calculateScores()
        self.wisdom = self.calculateScores()
        self.charisma = self.calculateScores()
        self.hitpoints = 10 + modifier(self.constitution)

    def calculateScores(self):
        from random import choice
        randomNumbers = [choice(range(1, 7)) for x in range(4)]
        return sum(randomNumbers) - min(randomNumbers)

def modifier(constitutionScore):
    return round((constitutionScore - 10) / 2)