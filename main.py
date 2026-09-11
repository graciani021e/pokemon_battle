import battle

class Main:
    battleManager = None
    def __init__(self):
        # print('Começou o jogo de monstros de bolso (por motivos autorais...)!\n\n')
        self.battleManager = battle.Battle()
        self.battleManager.start()
        pass    
    
Main()
        