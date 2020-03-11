# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, score=0, location='outside'):
        self.name = name
        self.score = score
        self.location = location
    def addScore(self, value):
        self.score += value
    def changeLocation(self, newLocation):
        self.location = newLocation

    
