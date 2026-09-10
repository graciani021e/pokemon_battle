import battle
import menu

class Main:
    battleManager = None
    def __init__(self):
        print('Welcome to the Pokemon Battle Game!\n\n')
        self.battleManager = battle.Battle()
        self.battleManager.startBattle()
        pass    
    
Main()
        