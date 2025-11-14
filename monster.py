class Monster():    
    pokemon = {
        "pikachu": {
            "name": "pikachu",
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
        "mewtwo": {
            "name": "mewtwo",
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
            "type": ["dark", "grass"],
            "hp": 100,
            "attack": 20,
            "defense": 40,
            "spattack": 100,
            "spdefense": 80,
            "speed": 110        
            }   
    }
    
    def getMonByName(self, mon):
        try:
            self.pokemon[mon]
        except:
            return "Digite Novamente"
        return self.pokemon[mon]
    
    def getMonByNumber(self, number):
        return {
            0: self.pokemon["pikachu"],
            1: self.pokemon["mewtwo"],
            2: self.pokemon["meowscarada"]
        }[number]
    
    def getMons(self):
        return self.pokemon.keys()
    
    def __init__(self):
        pass