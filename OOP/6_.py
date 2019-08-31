""" @property dan @setter """ 

class Player:
    def __init__(self, nama, umur):
        self.nama = nama # bisa juga self.nama = "MutiaSha" , nilai self.nama bisa juga langsung diisi nilainya, yg mana nilainya nanti dikembalikan pakai return self.nama pada sebuah funsgi
        self.umur = umur

    def info(self):
        return self.nama + " Umurnya " + self.umur

    @property # fungsinya bisa mengubah nilai variabel pada fungsi dengan mudah
    def informasi(self):
        return self.nama + " umurnya " + self.umur

    @informasi.setter #untuk mengganti nilai pada property
    def informasi(self, data):
        a, b = data.split(" ") #split untuk memisahakan data
        self.nama = a
        self.umur = b


abc = Player("Mutia", "20")

print(abc.info())
#property
abc.informasi = "MutiaSha 20"
print(abc.informasi)
