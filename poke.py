pokemon = {
    "pikachu": {
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
                "status": ""
            },
            "Thunder": {
                "type": "electric",
                "power": 70,
                "accuracy": 70,
                "priority": 1,
                "status": {"paralyzed": 10}
            }
        }
    }
}

#feito pelo gpt pq vai tomar no cu de digitar td isso
type_chart = {
    "normal": {
        "strong_against": [],
        "weak_against": ["rock", "steel"],
        "immune_against": ["ghost"]
    },
    "fire": {
        "strong_against": ["grass", "ice", "bug", "steel"],
        "weak_against": ["fire", "water", "rock", "dragon"],
        "immune_against": []
    },
    "water": {
        "strong_against": ["fire", "ground", "rock"],
        "weak_against": ["water", "grass", "dragon"],
        "immune_against": []
    },
    "electric": {
        "strong_against": ["water", "flying"],
        "weak_against": ["electric", "grass", "dragon"],
        "immune_against": ["ground"]
    },
    "grass": {
        "strong_against": ["water", "ground", "rock"],
        "weak_against": ["fire", "grass", "poison", "flying", "bug", "dragon", "steel"],
        "immune_against": []
    },
    "ice": {
        "strong_against": ["grass", "ground", "flying", "dragon"],
        "weak_against": ["fire", "water", "ice", "steel"],
        "immune_against": []
    },
    "fighting": {
        "strong_against": ["normal", "ice", "rock", "dark", "steel"],
        "weak_against": ["poison", "flying", "psychic", "bug", "fairy"],
        "immune_against": ["ghost"]
    },
    "poison": {
        "strong_against": ["grass", "fairy"],
        "weak_against": ["poison", "ground", "rock", "ghost"],
        "immune_against": ["steel"]
    },
    "ground": {
        "strong_against": ["fire", "electric", "poison", "rock", "steel"],
        "weak_against": ["grass", "bug"],
        "immune_against": ["flying"]
    },
    "flying": {
        "strong_against": ["grass", "fighting", "bug"],
        "weak_against": ["electric", "rock", "steel"],
        "immune_against": []
    },
    "psychic": {
        "strong_against": ["fighting", "poison"],
        "weak_against": ["psychic", "steel"],
        "immune_against": ["dark"]
    },
    "bug": {
        "strong_against": ["grass", "psychic", "dark"],
        "weak_against": ["fire", "fighting", "poison", "flying", "ghost", "steel", "fairy"],
        "immune_against": []
    },
    "rock": {
        "strong_against": ["fire", "ice", "flying", "bug"],
        "weak_against": ["fighting", "ground", "steel"],
        "immune_against": []
    },
    "ghost": {
        "strong_against": ["psychic", "ghost"],
        "weak_against": ["dark"],
        "immune_against": ["normal"]
    },
    "dragon": {
        "strong_against": ["dragon"],
        "weak_against": ["steel"],
        "immune_against": ["fairy"]
    },
    "dark": {
        "strong_against": ["psychic", "ghost"],
        "weak_against": ["fighting", "dark", "fairy"],
        "immune_against": []
    },
    "steel": {
        "strong_against": ["ice", "rock", "fairy"],
        "weak_against": ["fire", "water", "electric", "steel"],
        "immune_against": []
    },
    "fairy": {
        "strong_against": ["fighting", "dragon", "dark"],
        "weak_against": ["fire", "poison", "steel"],
        "immune_against": []
    }
}

def is_super_effective(attacker, defender):
    return defender in type_chart[attacker]["strong_against"]

def is_not_very_effective(attacker, defender):
    return defender in type_chart[attacker]["weak_against"]

def has_no_effect(attacker, defender):
    return defender in type_chart[attacker]["immune_against"]



def main():
    print(has_no_effect("normal", "ghost"))
    return 0

main()