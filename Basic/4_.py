"""
while syarat:
    lakukan sesuatu
    lakukan sesuatu
"""
count = 0
while count < 5:
    print("***") # b = b + 1 supaya terbatas
    count +=1 # count = count + 1 ||java and C#: count++ atau count += 1
else:
    print("looping selesai, looping sebanyak", count, "kali. nilai count nya sekarang " + str(count))
print()

i = 0
while i < 10:
    if i == 5:
        break
    print(i, end=" ") # end=" " buat ngeprint nilai kesamping bukan ke bawah
    i += 1
else:
    print("Looping selesai")
print()

i = 0
while True: #kondisi dalam loop akan jalan terus
    if i == 20:
        break
    print(i, end=" ")
    i += 1
print()
print()

orang = ['hilman', 'boss', 'komeng'] #list
text = 'python'
for nama in orang:
    print('nama namanya adalah: ', nama)
for huruf in text:
    print(huruf, end="||")
print()

a = 0
while a < 4:
    b = 0
    while b < a:
        print("*", end='')
        b = b + 1 # b += 1
    print()
    a +=1

print()

for i in range(0,3): # for (int i=0; i<3; i++)
    print("******")

for a in range(1,5): #range angka 1 sampai 5
    for b in range(1,5):
        c= a+b
        print(c, end=" ")
    print()

"""
x = int(input())
i = 1
while i <= x:
    j = i
    while j <= x:
        print(" ")
        j+=1
    k = 1
    while k<=2*i:
        print("*")
        k=k+1
    print()
    i+=1
"""
