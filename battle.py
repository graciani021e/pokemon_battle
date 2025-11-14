import monster
import pprint

class MonTeam:
    team = []
    def __init__(self, teamArr):
        for mon in teamArr:
            self.addToTeam(mon)
    
    def addToTeam(self, mon):
        # print(monster.Monster(mon))
        self.team.append(monster.Monster().getMon(mon))

    def getTeam(self):
        return self.team

# class Battle:
class Battle:
    
    def __init__(self):
        self.createTeam()
        pass
    
    def createTeam():
        team1 = MonTeam(["pikachu", "mewtwo"]).getTeam()
        pprint.pprint(team1)
        
Battle.createTeam()
    