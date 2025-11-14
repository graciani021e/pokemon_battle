import battle
import menu

class Main:
    MAX_TEAM_SIZE = 3
    battleManager = battle.Battle()
    
    def __init__(self):
        self.buildTeam()
        pass
    
    def buildTeam(self):
        while(self.battleManager.getTeamSize() < self.MAX_TEAM_SIZE):
            monNumber = int(input(menu.Menu().createMonSelectMenu()))
            self.battleManager.createTeam(monNumber)
    
Main()
        