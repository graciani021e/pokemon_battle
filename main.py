import battle
import monster
import pprint

class Main:
    def __init__(self):
        m = monster.Monster()
        t = list(m.getMons())
        pprint.pprint(t)
        # battle.Battle.startBattle()
        pass
    
Main()
        