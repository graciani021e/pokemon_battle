ACTION_TYPES = {
    1: "forfeit",
    2: "attack"
}

ACTION_FORFEIT = 1
ACTION_ATTACK = 2

class Action:

    #TODO: actionQueue = Fila de Ações "DoT, Paralyze, etc..."
    user = None
    type = None
    move = None
    target = None

    def __init__(self, data):
        self.user = data["user"]
        self.type = data["type"]
        self.move = data["move"]
        self.target = data["target"]
        pass

    def execute(self):
        print("TIPO QUAL ", ACTION_TYPES[self.type])

        if self.type == ACTION_ATTACK:
            print("ataque")
            self.damage(self.user.moves[self.move]["power"], 1)

        elif self.type == ACTION_FORFEIT:
            print("ff")
        pass

    #Dá dano baseado no contexto (dano direto ou DoT)
    #TODO: DoT
    def damage(self, amount, round): 
        print("AMOUNT DMG", amount)
        self.target.stats["hp"]-=amount
        pass