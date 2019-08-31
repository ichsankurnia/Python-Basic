"""
SEQUENCE : List[] - Tuples() - Dictionary{} - Sets
"""
#list
orang = ['mutia', 'shafira', 'chairunisa']
umur = [20,30,50,75,99]
mixed = [1, 'text', 0.25, "abcde"]
abc = [
    ["blablabla", 7837, 87],
    ["fsbfsjk", 787, 94],
    ["bsf", 67, 980], ["687346", 8098, 89]
]

for x in orang:
    print(orang)
for x in orang:
    print("-", x)
for a in orang[0]:
    print('nama2nya: ', a)
for a,b,c in abc: #kalau isi dalam list ada 3, berarti harus ada 3 juga yg di for in
    print(c, end=" ") #list jika ada list lagi di dalamnya kita bisa milih yg mau di print sesuai urutan list yg di dalam

print()
print(orang,umur,mixed)
del mixed[3]
umur[4] = "mutiaa"
print(umur)
print(orang[1], umur[4], mixed[2])
print()

#tuples : imutable(permanen) gabisa edit, delete, nambah
person = ('mutia', 'shafira', 'chairunisa') #ini tuples beda kurung dengan list
person2 = ['mutia', 'shafira', 'chairunisa']

print(len(person)) #len panjang tuples atau list, bisa juga max/min
print(list(person))
print(tuple(person)) #convert to tuples
print()

#Dictionary (Tidak imutable)=> key:value (index ga harus dari nol, tapi mengakses berdasarkan key)
data = {"name": "Mutia", "age": "20", "hobby": "coding"}

print("umurnya adalah", data["age"])
data["name"] = "MutiasSha"
data["dream"] = "Programer"
del data["hobby"]
print(data)
print("Dreamnya adalah " + data["dream"])

for key, value in data.items():
    print(key + " : " + value)
print()

#nested Dictionary
hmm = {
        1:{"name": "Mutia", "age": "20", "hobby": "coding"},
        2:{"name": "Shafira", "age": "12", "hobby": "gabut"}
      }

print(hmm[2]["name"])
print(hmm[1])
print(hmm)
for kunci, nilai in hmm.items():
    print("\nKeynya:", kunci)
    for kunci2 in nilai:
        print(kunci2 + " -", nilai[kunci2])

#Sets => di dalamnya ga boleh ada yg sama, ga bisa di akses berdasarkan index atau key
oop = {"mutia","boss","komen","mutia"}
oop.add("alex")
oop.remove("boss")
print(oop)
angka1 = {1,2,3,4,5}
angka2 = {4,5,6,7,8}
print(angka1 | angka2) # &(unutuk irisan), -(angka1 yg beda dari angka2/atau sebaliknya tergantung urutan), ^(unutuk angka yg tidak diirisan)
