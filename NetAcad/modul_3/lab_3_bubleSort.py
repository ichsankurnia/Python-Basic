myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    myList.append(val)

while swapped:
    swapped = False
    # dibikin len(mylist) - 1 supaya tidak melewati range dari list saat ingin disortir
    # ex: for i in range (4) => i bernilai 0,1,2,3 dan kondisional dibawah terdapat i+1
    # dimana nilai i = 4 yg  merupakan range yg paling besar dalam list itu
    # pengulangan akan terus dilakukan krn dalam while sampai semua kondisi terpnuhi
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print("\nSorted:")
print(myList)

"""
for i in range:
	if myList[i] > myList[i+1]:
		swap = true
		myList[i], myList[i+1] = myList[i+1], myList[i]

berarti:
myList = 3,7,5,1,6
nilai list i0 = 3 , i1 = 3, i2 = 5, i3 = 1, i4 = 6
for i in range(4):
	10 = 3 bandingkan dg i1 = 7
	if 3 > 7: => tidak terjadi swap (false)
		(x)

	lanjut ke i1 = 7 bandingkan dg i2 = 5
	if 7 > 5: => terjadi swap (true)
		(y) tukar posisi i1=7 dg i2=5 sehingga list sekarang menjadi 3 5 7 1 6

	lanjut ke i2 = 7 banding dg i3 = 1
	if 7 > 1: => terjadi swap (true)
		(y) tukar posisi i2=7 dg i3=1 sehingga menjadi 3 5 1 7 6

	lanjut ke i3 = 7 banding dg i4 = 6
	if 7 > 6: => terjadi swap (true)
		(y) tukar posisi i3=7 dg i4=6 sehingga menjadi 3 5 1 6 7

	
	for loop selesai krn cuma 4 kali pengulangan (range 4)
	krn for loop di dalam while, for loop akan kembali mengulang

	list saat ini 3 5 1 6 7

	balik ke i0=3 bandingkan dg i1=5
	if 3 > 5: => tidak terjadi swap (false)
		(x)

	lanjut ke i1 = 5 bandingkan dg i2 = 1
	if 5 > 1: => terjadi swap (true)
		(y) tukar posisi i1=5 dg i2=1 sehingga menjadi 3 1 5 6 7

	lanjut ke i2=5 bandingkan dg i3 = 6
	if 5 > 6: => tidak terjadi swap (false)
		(x)

	lanjut ke i3=6 bandingkan dg i4 = 7
	if 6 > 7: => tidak terjadi swap (false)
		(x)


	for loop selesai krn cuma 4 kali pengulangan (range 4)
	krn for loop di dalam while, for loop akan kembali mengulang

	loop saat ini 3 1 5 6 7

	balik ke i0=3 bandingkan dg i1=1
	if 3 > 1: => terjadi swap (true)
		(y) tukar posisi i0=3 dg i1=1 sehingga menjadi 1 3 5 6 7

	while berakhir krn if tidak memenuhi kondisi dan swap tidak akan true
"""