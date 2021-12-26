

from .Player import Player
from .Coach import Coach

class Team:
    def __init__(self, record: str, city: str, name: str, age: int, stadium: str, standing: int,captain=None, coach=None, roster={},):
        
        self.name = name
        self.record = record
        self.roster = roster
        self.captain = captain
        self.coach = coach
        self.coachInf = {}
        self.players = []
        self.city = city
        self.age = age
        self.stadium = stadium
        self.standing = standing


    def drop(self, obj):

        if type(obj) == Coach:
            self.coach = None
        elif type(obj) == Player:
            r = dict(self.roster)
            del r[obj.jNum]
            self.roster = r
        elif type(obj) == int:
            r = dict(self.roster)
            del r[obj]
            self.roster = r

    def add(self, obj):

        if type(obj) == Coach:
            self.coach = obj
            self.coachInf = obj.pack()
        else:
            if len(self.roster) == 15:
                return ValueError("Roster is full, drop a player")
            self.roster[obj.jNum] = obj.pack()
            self.players.append(obj)

    def getRecord(self):
        return "{}-{}".format(self.record[0], self.record[1])

    def getRoster(self):
        return self.roster

    def getSummary(self):
        return "The {} are the #{} team in the league, the head coach is {} and the roster consists of {} players. The team is headquartered in the city of {} and plays in the {} with a record of {}".format(self.name, self.standing, self.coach.name, len(self.roster), self.city, self.stadium, self.record) 