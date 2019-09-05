# def function(n):
	
# 	result = [n]
	
# 	for i in range(n-1):
# 		n = n/2
# 		result.append(n)

# 	return result

# if __name__ == '__main__':
# 	n = int(input())
	
# 	hasil = function(n)
# 	print(hasil)


""" N adalah oanjang karakter
Input N : 5
Input nilai : 1
Hasil 00100

N: 7
nilai : 12.35
Hasil 01235 """

# def function(n, nilai):

# 	string = ""
	
# 	nilai = nilai * 100

# 	mid = int(n/2)

# 	for i in range(n):
# 		if i < mid:
# 			string += "0"

# 	string += str(nilai)

# 	return string

# if __name__ == '__main__':
# 	n = int(input())
# 	nilai = int(input())
	
# 	hasil = function(n, nilai)
# 	print(hasil)




def function(kata):

	kata = kata[:len(kata)-2]
	
	return kata

if __name__ == '__main__':
	kata = input()
	
	hasil = function(kata)
	print(hasil)