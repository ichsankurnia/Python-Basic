#kalau cuma ingin ngeprint satu nama doang
# from modul import fungsi
# print(fungsi("MutiaSha"))

# from .modul import person, fungsi

import modul as kelas

print(kelas.person)
print(kelas.fungsi("MutiaSha"))
print()

import datetime
#http://docs.python.org/3/library/datetime.html
waktu = datetime.datetime.now()
waktu1 = datetime.datetime(2018,1,1)
print(waktu, "||", waktu1, "||", waktu.strftime("%d %B %Y"))

#Local dan Global Variabel

name = "Mutia" #global Variabel

def function():
    global name #kalau mau edit global Variabel harus di deklarasiin dulu
    name = name + " Shafira" #kalau udah dideklarasiin otomatis akan mengubah semua varibale name baik didalam maupun diluar
    print("akses dari dalam function " + name)

function()
print("akses dari luar function", name)
print()

"""
    Exceptions
"""
a = "hilman"
#try dan except(catch) untuk ngetest program yg belum yakin (program akan error)
#kalau ada yg error try tidak akan jalan, except akan mengeksekusi program
#wwww.tutorialspoint.com/python/python_exceptions.html
try:
    print(i + a)
except:
    print("Somethings was wrong in i + a")
