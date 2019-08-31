"""
FUNCTIONS
"""
def fungsi1():      #function
    print("===YOW===")

def fungsi2(text = "Mutia"):
    print("======")
    print(text)

def fungsi3(a, b):
    print("jumlah dari a + b = ", a + b)

def fungsi4(a, b):
    # return a + b
    c = a + b
    return c #bisa langsung return a + b

def fungsi5(name, age):
    print("Name: " + name + " - age: " + str(age))

#   *Args, **Kwargs
def fungsi6(*name): #di dalamnya terdapat multiple argument dalam satu variabel dikasih tand (*) pada variable tsb
    for a in name:
        print(a, end=" ")
    print()

def fungsi7(**nama): #di dalamnya terdapat multiple argument dalam satu variabel dalam bentuk Dictionary
    for index, nilai in nama.items():
        print(index + " - " + nilai)

fungsi1()
fungsi2()
fungsi2("Hei...")
fungsi3(3,-5)
print()

print("hasilnya : " + str(fungsi4(10,20))) #bentuk lain print("hasilnya: ", fungsi(10,20))
d = fungsi4(10,20)
print(d) #print lansgung / print(d + 50)
print(fungsi4(d,50)) #variabel d jadi parameter a pada fungsion
print()

fungsi5(age = 20, name = "Mutia")
print()

fungsi6("Mutia", "Shafira", 20)

fungsi7(Nama = "MutiasSha", Umur = str(20), Hobby = "Ngoding") #fungsi7(Nama = "MutiasSha", Umur = "20", Hobby = "Ngoding")
