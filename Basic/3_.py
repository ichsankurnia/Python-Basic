a = input("Sia namo e?? ")
b = input("Sudah punya pacar?? ")
c = input("Siapa namanya?? ")
print("hei..."+ a + " kamu " + b + " punya pacar ya. si " + c + " namanya")

print()

#boolean
d = "sekolahkoding"
print(d.isdigit())
print(d.isalnum())
orang = input("Agamanya gimana: ")
baik = True
rajin = True
if baik & rajin:
    if (orang == "rajin ibadah") | (orang == "bagus"):
        print("InsyaAllah Sukses.....!!!")
    else:
        print("belum tentu sukses ataupun gagal")
elif rajin & ((orang == "rajin ibadah") | (orang == "bagus")):
    print("belum tentu sukses ataupun gagal brohhh")
else:
    print("Gagal....!!!!")

print()

"""
If Else
==, <=, >=, &(and), |(or), !=(not)
if (x==y) & (x==z) | (arg..):
    print("arg...")
"""
angka1 = 10
angka2 = 20

if angka1 < angka2:
    print("yes: ", angka1, "lebih kecil dari " + str(angka2))
else:
    print("noooo")

uang = input("uang kamu berapa: Rp. ")
utang = 10000

if int(uang) < utang:
    print("wah maaf bos engga cukup, uangnya kurang: Rp.", utang-int(uang), ",00 lagi")
elif  int(uang) == utang:
    print("terimakasih sudah bayar, sisanya gada")
else:
    print("uangnya banyak juga, sisanya lumayan nih: Rp.", int(uang)-utang, ",00")
