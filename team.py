from pprint import pprint

import monster
import menu

class Team:
    team = []
    MAX_TEAM_SIZE = 3
    def __init__(self): #Sempre que usar new team, um time novo é criado
        print("Criando novo time")
        while(self.getTeamSize() < self.MAX_TEAM_SIZE):
            monNumber = int(input(menu.Menu().createMonSelectMenu()))
            self.addToTeam(monNumber)
        print(self.getTeam())
        pass

    #Adiciona pokemon ao time
    def addToTeam(self, mon):
        return self.team.append(monster.Monster().getMonByNumber(mon))

    #Retorna os nomes dos pokemons que estão no time
    def getTeam(self):
        return [mon["name"] for mon in self.team]

    #Retorna tamanho atual do time
    #TODO: Diminuir número assim que pokemon não tiver HP
    def getTeamSize(self):
        return len(self.team)