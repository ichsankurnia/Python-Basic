"""
    EXERCISE2
"""
player1 = {"name": "sengoku", "power": 90}
player2 = {"name": "trunks", "power": 100}

def train(player):
    player["power"] = player["power"] + 8 #player["power"] += 10

def attack(attacker, defender):
    if (attacker["power"] > defender["power"]):
        print("attack success! Congrats..", attacker["name"])
    else:
        print("attack failed! You are too weak", attacker["name"])

attack(player1,player2)
train(player1)
train(player1)
attack(player1,player2)
