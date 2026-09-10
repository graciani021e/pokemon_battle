import battle
import menu

class Main:
    battleManager = battle.Battle()

    def __init__(self):
        print('Welcome to the Pokemon Battle Game!')
        self.battleManager.startBattle()
        pass    
    
Main()
        