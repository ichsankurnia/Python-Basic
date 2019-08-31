"""
    EXERCISE2
"""
p1_name = input("input the name for player1 : ")
p2_name = input("input the name for player2 : ")
player1 = {"name": p1_name, "power": 90}
player2 = {"name": p2_name, "power": 100}

def startGame():
    print("What do you want to do? 1.Train player1 2.Train Player2. 3.Fight 4.CheckStatus 5.Exit ")
    training = input()
    if training == "1":
        trainplayer1(player1)
    elif training == "2":
        trainplayer2(player2)
    elif training == "3":
        fight(player1, player2)
    elif training == "4":
        status()
    else:
        exit()

def trainplayer1(a): # a = player1
    a["power"] = a["power"] + 8 #a["power"] += 10
    print("succses train player1,", a["name"], "power currently = ", a["power"])
    print()
    startGame()

def trainplayer2(b): # b = player2
    b["power"] = b["power"] + 8 #player["power"] += 10
    print("succses train player1,", b["name"], "power currently =", b["power"])
    print()
    startGame()

def fight(a, b):
    if (a["power"] > b["power"]):
        print("Congratulations", a["name"], "You won this battle..!")
    else:
        print("You loss", a["name"], "..! your powers", a["power"], "is too weak, go training now..!!!!")
    if (b["power"] > a["power"]):
        print("Congratulations", b["name"], "You won this battle..!")
    else:
        print("You loss", b["name"], "..! You was weak, go training now..!!!")
    print()
    startGame()

def status():
    for a, b in player1.items():
        print(a, " - " , b)
    print()
    for c, d in player2.items():
        print(c, " - ", d)
    print()
    startGame()

def exit():
    print("Bye .. Bye ...")

startGame()
