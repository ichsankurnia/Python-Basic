#Class dan Object

class Player:
    name = "Oscar" #golbal var
    def __init__(self, nama):
        self.x = nama #self.x = nama dari variabel nama yg telah diinisialisasikan pada __init__
        self.a = "" #nilai2 ini dipanggil pake function, megganti nilainya ga pek function
        self.b = 100 #atau self.b = b
        self.c = 0 #self.c = 809 , intinya semua nilai di init dipanggil menggunakan return self.c pada funsgiC

    def fungsiA(self):
        return self.a

    def fungsiB(self):
        return self.b

    def fungsiC(self):
        return self.c

    def getName(self): #self parameter wajib yg ada di function di dala kelas
        self.name = "Emboaba"
        return self.name #self.name = self.global variabel name

    def testName(self, nama): #nama variabel baru
        self.name = nama
        return self.name

#Inhiritance
class test(Player): #kelas test(Kelas Anak) mewariskan kelas Player(Kelas Induk)
    def testDoang(self, abcd):
        self.xxx = abcd
        return self.xxx


#diluar kelas
pemain = Player("Mutiasha") # mewakili nama kelasnyam || pemain = Object
print(pemain.x) # mengisi nilai pada variabe nama pada fungsi __init__ pada kelas induk yg isinya "Mutiasha"
print(pemain.name + " " + pemain.getName(), pemain.testName("Junior"))
print()

#Pake Inhiritance
hmm = test("")
print(hmm.name +" "+ hmm.getName(), "umurnya " + str(hmm.testDoang(29)), "tahun") # pake inhiritance methode yg terdapat pada class induk bisa di panggil pada kelas anak
print()

abc = test("")
abc.a = "Mutia Shafira Chairunisa"
abc.c = "Kekasihku"
print(abc.fungsiA(), "dia adalah", abc.fungsiC(), "perasaanku kedia", abc.fungsiB())
