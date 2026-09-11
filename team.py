import monster
import menu
import const
import random

class Team:
    
    team = []
    MAX_TEAM_SIZE = 3

    #Sempre que usar new team, um time novo é criado
    def __init__(self, player = True):
        self.team = [] #Reseta variável para não afetar o próximo player
        print("Criando novo time")
        if player:
            self.buildTeamPlayer()
        else:
            mode = int(input(menu.Menu().createModeMenu()))
            self.buildTeamBot(mode)
        pass

    #Adiciona um monstro ao time
    def addToTeam(self, monId):
        newMon = monster.Monster(monster.getMonById(monId))
        return self.team.append(newMon)

    #Retorna os nomes dos monstros que estão no time
    def getTeam(self):
        return [mon.name for mon in self.team]

    #Retorna tamanho atual do time
    #TODO: Diminuir número assim que um monstro não tiver HP
    def getTeamSize(self):
        return len(self.team)

    #Cria time do player usando interface de texto
    def buildTeamPlayer(self):
        while(self.getTeamSize() < const.TEAM["MAX_TEAM_SIZE"]): #Enquanto o time não estiver preenchido
            monId = int(input(menu.Menu().createMonSelectMenu())) #Captura ID do mon de acordo com digitado na interface
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

            #Seleciona um monsro entre varios outros do mesmo tier, como o resultado é o index eu acrescento em um para pegar o valor do tier
            chosenMon = random.choice(monster.getMonsByTier(highestPossiblePointChoice+1)) 
            self.addToTeam(chosenMon["id"])
            remainingPoints-= highestPossiblePointChoice+1 #decresce os pontos disponíveis pelo tier
        pass