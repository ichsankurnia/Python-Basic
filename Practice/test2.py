""" N adalah oanjang karakter
Input N : 5
Input nilai : 1
Hasil 00100

N: 7
nilai : 12.35
Hasil 01235 """

def function(n, nilai):

	string = ""
	
	nilai = int(nilai * 100)

	for i in range(n-len(nilai)):
		string += "0"

	string += str(nilai)

	return string

if __name__ == '__main__':
	n = int(input())
	nilai = float(input())
	
	hasil = function(n, nilai)
	print(hasil)