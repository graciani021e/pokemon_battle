import monster

class Menu:
    ACTIONS = {1: "attack", 2: "forfeit"}
    def __init__(self):
        pass
    
    def createMonSelectMenu(self):
        m = monster.Monster()
        message = "Digite o número do pokemon desejado (Max: 3)\n"
        for i, mon in enumerate(m.getMons()):
            message+= "{} - {}\n".format(i, mon.capitalize())
        message+= "10 - Sair\n"
        return message
    
    def createActionMenu(self):            
        message = "\n\n"
        for acIndex in self.ACTIONS:
            message+= "{} - {}\n".format(acIndex, self.ACTIONS[acIndex].capitalize())
        return message
    
    def createAttackMenu(self, menu, pokemon):
        i =1
        for move in pokemon["moves"]:
            print("{0} - {1}".format(i, move))
            i+=1
    