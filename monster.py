import const


class Monster():    

    def __init__(self):
        pass

    monster = {
        "pikachu": {
            "name": "pikachu",
            "id": 1,
            "tier": const.TIERS["basic"],
            "type": ["electric"],
                "hp": 74,
                "attack": 55,
                "defense": 40,
                "spattack": 50,
                "spdefense": 50,
                "speed": 90,
                "moves": {
                    "Quick attack" : {
                        "type": "normal",
                        "power": 50,
                        "accuracy": 100,
                        "priority": -1,
                        "status": "",
                        "pp": 25 #TODO: PP ENDING
                    },
                    "Thunder": {
                        "type": "electric",
                        "power": 70,
                        "accuracy": 70,
                        "priority": 1,
                        "status": {"paralyzed": 10},
                        "pp": 25 #TODO: PP ENDING
                    }
                }
            }, 
        "caterpie": {
            "name": "caterpie",
            "id": 2,
            "tier": const.TIERS["basic"],
            "type": ["bug"],
                "hp": 45,
                "attack": 30,
                "defense": 40,
                "spattack": 50,
                "spdefense": 50,
                "speed": 90,
                "moves": {
                    "Quick attack" : {
                        "type": "normal",
                        "power": 50,
                        "accuracy": 100,
                        "priority": -1,
                        "status": "",
                        "pp": 25 #TODO: PP ENDING
                    },
                    "Thunder": {
                        "type": "electric",
                        "power": 70,
                        "accuracy": 70,
                        "priority": 1,
                        "status": {"paralyzed": 10},
                        "pp": 25 #TODO: PP ENDING
                    }
                }
            }, 
        "mewtwo": {
            "name": "mewtwo",
            "id": 3,
            "tier": const.TIERS["godlike"],
            "type": ["psychic"],
            "hp": 120,
            "attack": 20,
            "defense": 70,
            "spattack": 100,
            "spdefense": 80,
            "speed": 120,
            "moves": {
                "Psychic": {
                    "type": "psychic",
                    "power": 70,
                    "accuracy": 100,
                    "priority": 1,
                    "status": "",
                    "pp": 20
                },
                "Shadow ball": {
                    "type": "dark",
                    "power": 65,
                    "accuracy": 90,
                    "priority": 1,
                    "status": "",
                    "pp": 20
                }
            }
        },
        "meowscarada": {
            "name": "meowscarada",
            "id": 4,
            "tier": const.TIERS["medium"],
            "type": ["dark", "grass"],
            "hp": 100,
            "attack": 20,
            "defense": 40,
            "spattack": 100,
            "spdefense": 80,
            "speed": 110        
            }   
    }
    

    #Começo funções de ataque
    



    #getAttackModifier("normal", "ghost") = 0
    #getAttackModifier("fire", "water") = 0.5
    #getAttackModifier("water", "fire") = 2
    #danofinal = danoataque * getAttackModifier
    #



def getMonByName(self, mon):
    try:
        self.monster[mon]
    except:
        return "Digite Novamente"
    return self.monster[mon]

def getName(self, mon):
    return self.monster[mon]["name"]

def getMonById(self, id):
    return [mon for mon in self.monster.values() if mon["id"] == id][0]

def getMonsByTier(self, tier):
    return [mon for mon in self.monster.values() if mon["tier"] == tier]

def getMons(self):
    return [{"id": mon["id"], "name": mon["name"]} for mon in self.monster.values()]