import monster

class Team:
    team = []
    def __init__(self):
        pass
    
    def addToTeam(self, mon):
        self.team.append(monster.Monster().getMonByNumber(mon))

    def getTeam(self):
        return self.team