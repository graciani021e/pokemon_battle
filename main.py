import battle
import monster
import pprint

class Main:
    MAX_TEAM_SIZE = 3
    battleManager = battle.Battle()
    def __init__(self):
        while(self.battleManager.getTeamSize() < self.MAX_TEAM_SIZE):
            monNumber = int(input(self.createMonSelectMenu()))
            self.battleManager.createTeam(monNumber)
        pass
    
    
    def createMonSelectMenu(self):
        m = monster.Monster()
        message = "Digite o número do pokemon desejado (Max: 3)\n"
        for i, mon in enumerate(m.getMons()):
            message+= "{}- {}\n".format(i, mon.capitalize())
        i+=1
        message+= "{} - Terminar escolha de time".format(i)
        i+=1
        message+= "{} - Sair".format(i)
        return message
    
    
Main()
        