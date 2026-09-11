import monster
import const
import action
import battle

def createMonSelectMenu():
    print(monster.getMons())
    message = "Digite o número do monstro desejado (Max: 3)\n"
    for mon in monster.getMons():
        message+= "{} - {}\n".format(mon["id"], mon["name"].capitalize())
    message+= "10 - Sair\n"
    return message

def createActionMenu():            
    message = "\n\n"
    for acIndex in action.ACTION_TYPES:
        message+= "{} - {}\n".format(acIndex, action.ACTION_TYPES[acIndex].capitalize())
    return message

def createModeMenu():            
    message = "\n\n"
    for acIndex in battle.BOT["MODES"]:
        message+= "{} - {}\n".format(acIndex, battle.BOT["MODES"][acIndex].capitalize())
    return message

def createAttackMenu(menu, monster):
    i =1
    for move in monster.moves:
        print("{0} - {1}".format(i, move))
        i+=1
    