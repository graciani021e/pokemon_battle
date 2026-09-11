import monster
import const

class Menu:
    def __init__(self):
        pass
    
    def createMonSelectMenu(self):
        print(monster.getMons())
        message = "Digite o número do monstro desejado (Max: 3)\n"
        for mon in monster.getMons():
            message+= "{} - {}\n".format(mon["id"], mon["name"].capitalize())
        message+= "10 - Sair\n"
        return message
    
    def createActionMenu(self):            
        message = "\n\n"
        for acIndex in const.ACTIONS:
            message+= "{} - {}\n".format(acIndex, const.ACTIONS[acIndex].capitalize())
        return message
    
    def createModeMenu(self):            
        message = "\n\n"
        for acIndex in const.BOT["MODES"]:
            message+= "{} - {}\n".format(acIndex, const.BOT["MODES"][acIndex].capitalize())
        return message
    
    def createAttackMenu(self, menu, monster):
        i =1
        for move in monster["moves"]:
            print("{0} - {1}".format(i, move))
            i+=1
    