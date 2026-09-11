import team
import menu
import action

BOT = {
    "MODES": {
        1: "easy",
        2: "medium",
        3: "hard",
    },
    "TEAM_POINTS": { 
        "easy": 3,
        "medium": 5,
        "hard": 7,
    }
}

class Battle:
    playerTeam = []
    opponentTeam = []
    teamManager = None
    turn = 0
    def __init__(self):
        self.playerTeam = team.Team()
        self.opponentTeam = team.Team(player=False)
        # print("Player Team: {}".format(self.playerTeam.getTeam()))
        # print("Opponent Team: {}".format(self.opponentTeam.getTeam()))
        pass
            
    def start(self):
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
        #TODO: Selecionar pokemon para realizar acao
        print("startFunction")
        print("HP ANTES DO DANO", self.opponentTeam.team[0].stats["hp"])
        actionId = int(input(menu.createActionMenu()))
        context = {
            "user": self.playerTeam.team[0],
            "type": actionId,
            "move": "Thunder",
            "target": self.opponentTeam.team[0]
        }
        actionFinal = action.Action(context)
        actionFinal.execute()
        print("HP DEPOIS DO DANO", self.opponentTeam.team[0].stats["hp"])
        pass



    
    