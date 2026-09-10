from pprint import pprint

import monster
import menu
import const
import random
import numpy as np

class Team:
    team = []
    MAX_TEAM_SIZE = 3
    def __init__(self, player = True): #Sempre que usar new team, um time novo é criado
        self.team = []
        print("Criando novo time")
        if player:
            self.buildTeamPlayer()
        else:
            mode = int(input(menu.Menu().createModeMenu()))
            self.buildTeamBot(mode)
        pass

    #Adiciona pokemon ao time
    def addToTeam(self, monId):
        return self.team.append(monster.Monster().getMonById(monId))

    #Retorna os nomes dos pokemons que estão no time
    def getTeam(self):
        return [mon["name"] for mon in self.team]

    #Retorna tamanho atual do time
    #TODO: Diminuir número assim que pokemon não tiver HP
    def getTeamSize(self):
        return len(self.team)

    def buildTeamPlayer(self):
        while(self.getTeamSize() < const.TEAM["MAX_TEAM_SIZE"]):
            monId = int(input(menu.Menu().createMonSelectMenu()))
            self.addToTeam(monId)
        print(self.getTeam())
        pass

    #Cria time do bot de acordo com o modo escolhido
    def buildTeamBot(self, mode):
        remainingPoints = const.BOT["TEAM_POINTS"][const.BOT["MODES"][mode]] #Pontos disponíveis de acordo com o tier escolhido
        while(self.getTeamSize() < const.TEAM["MAX_TEAM_SIZE"]): #Enquanto o time não estiver preenchido

            #Captura o tier aproximado de acordo com a quantidade de time preenchido e pontos que o bot ainda tem, resultado é o INDEX do tier que ele vai pegar
            highestPossiblePointChoice = min(range(len(const.TIERS)),
            key=lambda 
            i: abs(list(const.TIERS.values())[i] - (remainingPoints/(const.TEAM["MAX_TEAM_SIZE"]-self.getTeamSize()))))

            #Seleciona um pokemon entre varios outros do mesmo tier, como o resultado é o index eu acrescento em um para pegar o valor do tier
            chosenMon = random.choice(monster.Monster().getMonsByTier(highestPossiblePointChoice+1)) 
            self.addToTeam(chosenMon["id"])
            remainingPoints-= highestPossiblePointChoice+1 #decresce os pontos disponíveis pelo tier
        pass