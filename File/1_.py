# FILE I/O
# http://docs.pyhton.org/3/library/functions.html
# file harus satu folder
"""
file = open("data.txt", "r") # r = read
file2 = open("data.txt", "w") # w = write

file2.write("indak ka mungkin kito babagi rasooo") #ganti isi dari data.txt
text = file2.read()  # read data.txt tapi di open yg "w" ganti jadi" r"
print(text) """

def start():
    print("Apa yang ingin anda lakukan? 1.Belanja, 2.LihatDaftarBelanja, 3.KosongkanDaftarBelanja, 4.Exit ")
    do = input()
    if do == "1":
        add_to_list(input("Mau belanja apa? ")) # newText = input("Mau jajan apa? ")
    elif do == "2":
        daftarBelanja()
    elif do == "3":
        kosongkan("")
    else:
        exit()

def add_to_list(newText): # newText = input("Mau belanja apa? ") hasil dari newText di tulis ke data.txt
    with open("data.txt", "a+") as file: # a+= walaupun ditambahkan fungsi write isi file yg sebelumnya tidak akan hikang
        file.write("\n" + newText)
    print("Apakah anda mau belanja lagi? 1.Ya, 2.Tidak ")
    did = input()
    if did == str(1):
        ask_user() #ctrl + enter close the terminal
    else:
        start()

def ask_user():
    add_to_list(input("Mau jajan apa lagi? ")) # newText = input("Mau jajan apa? "), panggil lagi fungsi add_to_list(newText)

def daftarBelanja():
    print("Daftar Belanja saat ini: ")
    file2 = open("data.txt", "r")
    text = file2.read()
    print(text)
    start()

def kosongkan(remove):
    print("Apa anda yakin untuk menghapus daftar belanja saat ini? 1.Ya || 2.Tidak")
    rmv = input()
    if rmv == "1":
        with open("data.txt", "w") as file:
            file.write(remove)
        print("Sukses mengkosongkan daftar belanja")
        daftarBelanja()
    else:
        print("Daftar belanja tidak jadi dikosongkan")
        start()

def exit():
    print("Bye .. Bye ...")

start()  #function yg dijalankan pertama
