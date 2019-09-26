# Tugasmu adalah mempersiapkan kode simpel untuk menentukan waktu akhir/selesai sebuah kegiatan.
# Diberikan variabel durasi waktu dalam menit dan waktu mulai dalam jam (0..23)dan menit (0..59).
# sebagai contoh, jika suatu kegiatan dimulai pukul `12:17` dan berlangsung selama `59 minutes` , 
# maka kegiatan tersebut tersebut akan selesai pukul `13:16`

jam = int(input("Jam sekarang: "))
menit = int(input("Menit sekarang: "))
durasi = int(input("Jumlah durasi: "))

if durasi > menit:
	jam += int((menit+durasi)/60)

menit += durasi%60

print(str(jam%24) + ":" + str(menit%60))