import monster
import pprint

class MonTeam:
    team = []
    def __init__(self, teamArr):
        for mon in teamArr:
            self.addToTeam(mon)
    
    def addToTeam(self, mon):
        self.team.append(monster.Monster().getMon(mon))

    def getTeam(self):
        return self.team

# class Battle:
class Battle:
    playerTeam = []
    def __init__(self):
        pass
    
    def createTeam(self, team):
        team = team.split(",")
        self.playerTeam = MonTeam(team).getTeam()
        print(self.playerTeam)
        
    def startBattle(self, team):
        self.createTeam(team)
        
    
    