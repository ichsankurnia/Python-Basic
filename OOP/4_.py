# class Player:
#     def __init__(self):
#         self.age = 23
#
# class KelasLain(Player): #inhiritance
#     pass
#
# aaa = KelasLain()
# print(aaa.age)

class Player:
    def __init__(self, name):
        self.name = name # isa juga self.name = "MutiaSha"
        self._age = 23
        self.__umur = 20 #nilai permanen gabisa diubah cuma bisa ditampilkan pake function

    def getName(self):
        return self.name

    def getUmur(self):
        return self.__umur

class KelasLain(Player): #inhiritance
    pass

abc = KelasLain("nnsfnl")
abc.name = "mutia" #hanya bisa diubah jika dia dalam __init__, jika tidak dalam init gunakan fnction untuk menggantinya
abc.__umur = 25 #nilai tidak akan berubah
abc._Player__umur = 25 #cara mengubah nilai yg di private
print(abc._age, abc.getName(), abc.getUmur())
