import pprint
import team
import menu

class Battle:
    playerTeam = []
    teamManager = None
    menuManager = None
    turn = 0
    def __init__(self):
        self.teamManager = team.Team()
        self.menuManager = menu.Menu()
        pass
            
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
    