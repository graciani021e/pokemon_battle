import monster
class Menu:    
    def __init__(self):
        pass
    
    def createMonSelectMenu(self):
        m = monster.Monster()
        message = "Digite o número do pokemon desejado (Max: 3)\n"
        for i, mon in enumerate(m.getMons()):
            message+= "{} - {}\n".format(i, mon.capitalize())
        message+= "10 - Sair\n"
        return message