import const


class Monster():  

    name = ""  
    types = []
    stats = {
        "hp": 0,
        "attack": 0,
        "defense": 0,
        "spAttack": 0,
        "spDefense": 0,
        "speed": 0,
    }
    moves = []

    #Data é o objeto do monstro
    def __init__(self, data):
        self.name = data["name"]
        self.types = data["types"]
        self.stats = data["stats"]
        self.moves = data["moves"]

        print("pokemon data")
        print(self.name, self.types, self.stats, self.moves)
        pass


monster = {
    "pikachu": {
        "name": "pikachu",
        "id": 1,
        "tier": const.TIERS["basic"],
        "types": ["electric"],
        "stats": {
            "hp": 74,
            "attack": 55,
            "defense": 40,
            "spattack": 50,
            "spdefense": 50,
            "speed": 90,
        },
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
        "types": ["bug"],
        "stats": { 
            "hp": 45,
            "attack": 30,
            "defense": 40,
            "spattack": 50,
            "spdefense": 50,
            "speed": 90,
        },
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
        "types": ["psychic"],
        "stats": {
            "hp": 120,
            "attack": 20,
            "defense": 70,
            "spattack": 100,
            "spdefense": 80,
            "speed": 120,
        },
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
        "types": ["dark", "grass"],
        "stats": {
            "hp": 100,
            "attack": 20,
            "defense": 40,
            "spattack": 100,
            "spdefense": 80,
            "speed": 110  
        },
        
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
    }   
}

def getMonByName(mon):
    try:
        monster[mon]
    except:
        return "Digite Novamente"
    return monster[mon]

def getName(mon):
    return monster[mon]["name"]

def getMonById(id):
    return [mon for mon in monster.values() if mon["id"] == id][0]

def getMonsByTier(tier):
    return [mon for mon in monster.values() if mon["tier"] == tier]

def getMons():
    return [{"id": mon["id"], "name": mon["name"]} for mon in monster.values()]


#getAttackModifier("normal", "ghost") = 0
#getAttackModifier("fire", "water") = 0.5
#getAttackModifier("water", "fire") = 2
#danofinal = danoataque * getAttackModifier