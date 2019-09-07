def function(kata):

	kata = kata[:len(kata)-2]
	
	return kata

if __name__ == '__main__':
	kata = input()
	
	hasil = function(kata)
	print(hasil)