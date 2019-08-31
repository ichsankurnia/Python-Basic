""" @staticmethod dan @classmethod """

class Player:
    job = "Programer"

    def __init__(self, name): #nama, speed, balance ga harus inisialisasikan di awal atau dijadikan global variabel
        self.name = name # bisa juga self.name = "MutiaSha"

    def getName(self):
        return self.name

    # classmethod && staticmethod
    @staticmethod
    def pensiun(age):
        return 60 - age # str(60 - age)

    @classmethod
    def info(cls):
        return cls.job + " akan pensiun dalam 60 tahun"

    @classmethod
    def infoLain(cls, umur): #umur = age pada fungsi pensiun(age)
        return cls.job + "ini akan pensiun dalam " + str(cls.pensiun(umur)) + " tahun"

print("Pensiun dalam " + str(Player.pensiun(20)) + " tahun")
print()
print(Player.info())
print()
print(Player.infoLain(40))
