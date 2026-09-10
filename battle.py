import team
import menu

class Battle:
    playerTeam = []
    opponentTeam = []
    teamManager = None
    turn = 0
    def __init__(self):
        self.playerTeam = team.Team()
        self.opponentTeam = team.Team(player=False)
        print("Player Team: {}".format(self.playerTeam.getTeam()))
        print("Opponent Team: {}".format(self.opponentTeam.getTeam()))
        pass
            
    def startBattle(self):
        self.fight = True
        while(self.fight == True):
            self.doTurn()
            self.fight = False
            self.changeTurn()
            
    def changeTurn(self):
        if self.turn == 1:
            self.turn = 0
        else:
            self.turn = 1
            
    def doTurn(self):
        action = input(menu.createActionMenu())
    