class Player:

    mutia = "Mutia Shafira"
    sha = "Chairunisa"

    def ambilSkill(self):
        return "Jago"

#Inhiritance ( Mewariskan Kelas)
class ChelseaPlayer(Player):

    #jika mau bikin suatu otomatis(ex: otomatis ngeprint suatu kalimat) bikin function __init__
    def __init__(self): #inisialisasi awal
        # Player.__init__(self, a)\
        super().__init__() #super mengakses metode dari parentnya, ga perlu dipadang self lagi
        print("Quick")

    sha = 100 #override, nilai sha pada parent diganti dengan yg ada pada kelas anak

    def ambilSkill(self):
        return "Pintar"

    def test(self, abc):
        self.abc = abc
        return self.abc

pemain = ChelseaPlayer()
pemain.sha = "100%"
print(pemain.mutia + "", pemain.ambilSkill(), pemain.test("Hebat"), pemain.sha)
