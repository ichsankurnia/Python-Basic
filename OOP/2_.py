class Player:
    def __init__(self, nama, speed, shoot): #nama, speed, balance ga harus inisialisasikan di awal atau dijadikan global variabel
        self.nama = nama # bisa juga self.name = "MutiaSha"
        self.speed = speed # bisa juga self.speed = 90
        self.shoot = shoot 

    def ambilName(self):
        return self.nama

    def ambilSpeed(self):
        return self.speed

    def ambilShoot(self):
        return self.shoot

    def ambilSkill(self):
        return "Normal"

#Inhiritance ( Mewariskan Kelas)
class ChelseaPlayer(Player):
    def setAge(self, age):
        self.age = age
        return self.age

    def testDoang(self, abcd):
        self.xxx = abcd
        return self.xxx

    def ambilSkill(self):
        return "Jago"

class LiverpoolPlayer(Player):
    #jika mau bikin suatu otomatis(ex: otomatis ngeprint suatu kalimat) bikin function __init__
    def __init__(self, a, b, c): #inisialisasi awal
        # Player.__init__(self, a)\
        super().__init__(a, b, c) #super mengakses metode dari parentnya, ga perlu dipadang self lagi
        print("Hellow LiverpoolPlayer")

    def setAge(self, age):
        self.age = age
        return self.age

    def ambilSkill(self, skill):
        self.skill = skill
        return self.skill

#dari kelas induk
pemain = Player("Oscar", 85, 90)
print(pemain.ambilName() + " punya speed " + str(pemain.ambilSpeed()) + " dan tembakannya", pemain.ambilShoot())
print()

#pake Inhiritance
hmm = ChelseaPlayer("","","") #harus diisi argumen, tidak boleh kosong karna dikelas induk ada fungsi __init__ yang menginisialisasikan semua
print("Gejeeeeee " + str(hmm.testDoang(0.0000322323)))
pemain2 = ChelseaPlayer("Hazzard", 90, 86) #__init__nya tetap ngambil dari
print(pemain2.ambilName(), "umurnya", pemain2.setAge(30), "punya speed", pemain2.ambilSpeed(), "dan tembakannya", pemain2.ambilShoot())
pemain3 = LiverpoolPlayer("Firmino", 88, 88)
print(pemain3.ambilName(), "umurnya", pemain3.setAge(26), "punya speed", pemain3.ambilSpeed(), "dan tembakannya", pemain3.ambilShoot())
print()

#Override jika ada fungsi yang sama dengan fungsi pada kelas induk, maka nilai yg diambil dari fungi kelas anak, contoh disini adalah fungsi ambilSkill()
a = ChelseaPlayer("Mute","","sha")
print("Nama", a.ambilName(), "Skillnya", a.ambilSkill(), "nama lainnya", a.ambilShoot())
b = LiverpoolPlayer("","Chairunisa","Shafira")
print(b.ambilShoot(), "namanya,", b.ambilSpeed(), "nama panjangnya, kelebihanya", b.ambilSkill("Visual Studio dan C#"))
