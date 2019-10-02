""" Soal Nomor 1 """
# x = int(input())
# y = 3*x**3 - 2*x**2 +9*x - 410
# print(y)

""" soal nomor 2 """

# class Kardus:
#     def __init__(self, panjang, lebar, tinggi):
#         self.panjang = panjang
#         self.lebar = lebar
#         self.tinggi = tinggi

#     def volumeKardus(self):
#         return self.panjang * self.lebar * self.tinggi

#     def luasPermKarsus(self):
#         perm = 2*(self.panjang*self.lebar + self.panjang*self.tinggi + self.tinggi*self.lebar)

#         return perm

#     def massaJenis(self,massa):
#         return massa/self.volumeKardus()

# KotakBiru = Kardus(10,8,4)
# KotakMerah = Kardus(15,5,1)

# print(KotakBiru.volumeKardus(), KotakBiru.luasPermKarsus(), KotakBiru.massaJenis(1))
# print(KotakMerah.volumeKardus(), KotakMerah.luasPermKarsus(), KotakMerah.massaJenis(1))


""" Soal Nomor 3 """

# dic = {"001": "Bahasa Indonesia",
#        "002": "Bahasa Inggris",
#        "003": "Matematikas",
#        "004": "Biologi",
#        "005": "Fisika"}
#
# dic["003"] = "Kimia"
# dic["005"] = "Olahraga"
#
# for i in range(6,11):
#     mapel = input("Masukan Mata Pelajaran Baru: ")
#     dic["00"+str(i)] = mapel
#
# for keys, val in dic.items():
#     print(keys + " ==> " + val)


""" Soal Nomor 4 """

# popDigital = float(input("Populasi Kota Digital: "))
# popTalent = float(input("Populasi Kota Talent: "))
#
# rateDigital = float(input("Rate Pertumbuhan Kota Digital: "))
# rateTalent = float(input("Rate Pertumbuhan Kota Talent: "))
#
# tahunSekarang = 2019
#
# while 1:
#     a = popDigital * rateDigital
#     popDigital += a
#
#     b = popTalent * rateTalent
#     popTalent += b
#
#     tahunSekarang += 1
#     if popTalent > popDigital:
#         break
#
# print("Tahun :", tahunSekarang)
# print("Populasi Digital", popDigital)
# print("Populasi Talent", popTalent)


""" Soal Nomor 5 """
"""
Budi tertarik untuk melamar pekerjaan pada liburan semester yang akan berlangsung selama 5 minggu.
Gaji yang diberikan adalah gaji per jam. Total pajak yang harus budi bayarkan dari penghasilannya selama bekerja adalah 14%.
Setelah membayar pajak, budi menghabiskan 10% dari pendapatan bersihnya untuk membeli baju dan aksesoris yang akan digunakan pada semester baru,
dan 1% untuk membeli alat tulis. Setelah membeli baju, aksesoris dan alat tulis, Budi menggunakan 25% dari sisa uangnya untuk disedekahkan.
Setiap Rp.1000 yang Budi sedekahkan 30% nya akan diserahkan kepada anak yatim, dan sisanya akan diserahkan ke kaum dhuafa.

Buatlah sebuah program, dengan input:
Gaji per jam yang anda inginkan
Jumlah jam kerja yang akan dilakukan dalam 1 minggu

Output dari program adalah sebagai berikut :
Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak.
Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak.
Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris.
Jumlah uang yang akan Budi habiskan untuk membeli alat tulis.
Jumlah uang yang akan Budi sedekahkan.
Jumlah uang yang akan diterima anak yatim.
Jumlah uang yang akan diterima kaum dhuafa.
"""
# gaji_per_jam = float(input("Gaji per jam yang anda inginkan: "))
# jam = int(input("Jumlah jam kerja yang akan dilakukan dalam 1 minggu: "))
# jmlh_minggu = 5
#
# gaji_kotor = gaji_per_jam * jam * jmlh_minggu
# gaji_bersih = gaji_kotor * (100-14)/100
# baju = gaji_bersih * 10/100
# alat_tulis = gaji_bersih * 1/100
# sedekah = (gaji_bersih - baju - alat_tulis) * 25/100
# anak_yatim = sedekah * 30/100
# kaum_dhuafa = sedekah - anak_yatim
#
#
# print("Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak", gaji_kotor)
# print("Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak", gaji_bersih)
# print("Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris", baju)
# print("Jumlah uang yang akan Budi habiskan untuk membeli alat tulis", alat_tulis)
# print("Jumlah uang yang akan Budi sedekahkan", sedekah)c
# print("Jumlah uang yang akan diterima anak yatim", anak_yatim)
# print("Jumlah uang yang akan diterima kaum dhuafa", kaum_dhuafa)


""" Soal Nomor 6 """
"""
Pada sebuah Mall, biaya parkir adalah 3.000 untuk dua jam pertama baik motor maupun mobil,
setelah itu dikenakan biaya setiap jam 2.000 untuk motor dan 4.000 untuk mobil.
Adapun terdapat larangan parkir lebih dari 24 jam sehingga bila pengunjung parkir lebih dari
24 jam akan dikenakan denda tambahan 100.000 setiap 24 jam.

Buatlah sebuah program yang menerima input berupa jam parkir, beserta keluaran merupakan biaya parkir
"""

# motor = mobil = 3000
# jam = int(input("Jam parkir: "))
#
# i = 0
#
# for i in range(1,jam+1):
#     if i > 2:
#         motor += 2000
#         mobil += 4000
#
#         if i % 24 == 0:
#             i -= 24
#             motor += 100000
#             mobil += 100000
#     print(i)
#
# print("Biaya Parkir Motor: ", motor)
# print("Biaya Parkir Mobil: ", mobil)
