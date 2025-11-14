import monster
import pprint

class MonTeam:
    team = []
    def __init__(self):
        pass
    
    def addToTeam(self, mon):
        self.team.append(monster.Monster().getMonByNumber(mon))

    def getTeam(self):
        return self.team

class Battle:
    playerTeam = []
    monTeamManager = MonTeam()
    def __init__(self):
        pass
    
    def createTeam(self, monnumber):
        self.monTeamManager.addToTeam(monnumber)
        self.playerTeam = self.monTeamManager.getTeam()
        pprint.pprint(self.playerTeam)
        
    def startBattle(self, team):
        self.createTeam(team)
        
    def getTeamSize(self):
        return len(self.monTeamManager.getTeam())
    
    