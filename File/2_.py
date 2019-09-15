import csv

""" Membaca File CSV pada Python """
array = [] #array

with open("file.csv", "r") as csvfile: #with untuk streaming file, secara otomatis akan close bersihin file saat ga di pake lagi
    csvreader = csv.DictReader(csvfile) #bentuk dictionary
    # csvreader = csv.reader(csvfile) #bentuk normal
    # for x in csvreader: #buat coment ctrl + /
    #      array.append(x)
    array = list(csvreader)
    print("total baris : ", csvreader.line_num, "\n")

for x in array[-5:]: #membatasi cuma membaca 5 data
    # print(x[0] + " - " + x[1]) # dalam list
    print(x["nama"] + " - " + x["skill"]) #dalam dictionary

print()

print(array)


"""Menulis File CSV pada python"""

array = [{"nama" : "Mutia", "skill" : "Program", "grade" : 90},
        {"nama" : "Shafira", "skill" : "Coding", "grade" : 95,},
        {"nama" : "Chairunisa", "skill" : "Gabut", "grade" : 80,}]

with open("file.csv", "a") as csvfile: # to delete all rows with new rows documente replace "a" to "W"
        fields = ["nama", "skill", "grade"]
        writer = csv.DictWriter(csvfile, fieldnames = fields)

        writer.writeheader()
        writer.writerows(array)
