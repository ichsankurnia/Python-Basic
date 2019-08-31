"""
    EXERCISE
"""
name = input("Nama monsternya siapa? ")
monster = {"name": name, "power": 80} #Dictionary , global variabel

def startGame():
    choise = input("What do you want to do? 1.Eat 2.CheckStatus 3.Keluar ")
    if choise == "1":
        goEat()
    elif choise == str(2):
        goStatus()
    else:
        goExit()

def goEat():
    print("Nyam .. Nyam ... ")
    monster["power"] += 5 #monster["power"] + 5
    print("Your power have increases")
    startGame()

def goStatus():
    print("Check .. Check ... ")
    print(monster) #buat nampilin semua Dictionary
    #print(monster["power"]) atau print(monster["name"])
    startGame()

def goExit():
    print("Bye.. Bye ... ")

startGame()
