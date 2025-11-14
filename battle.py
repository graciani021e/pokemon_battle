import pprint
import team
import menu

class Battle:
    playerTeam = []
    teamManager = team.Team()
    menuManager = menu.Menu()
    fight = False
    turn = 0
    def __init__(self):
        pass
    
    def createTeam(self, monnumber):
        if monnumber == 10:
            exit()
        self.teamManager.addToTeam(monnumber)
        self.playerTeam = self.teamManager.getTeam()
        pprint.pprint(self.playerTeam)
        
    def startBattle(self):
        self.fight = True
        while(self.fight == True):
            self.doTurn()
            self.fight = False
            self.changeTurn()
        
    def getTeamSize(self):
        return len(self.teamManager.getTeam())
    
    def changeTurn(self):
        if self.turn == 1:
            self.turn = 0
        else:
            self.turn = 1
            
    def doTurn(self):
        action = input(self.menuManager.createActionMenu())
    