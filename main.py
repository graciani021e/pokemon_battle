import battle

class Main:
    battleManager = None
    def __init__(self):
        print('Welcome to the Pokemon Battle Game!\n\n')
        self.battleManager = battle.Battle()
        pass    
    
Main()
        