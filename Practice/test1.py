def function(n):
	
	result = [n]
	
	for i in range(n-1):
		n = n/2
		if n > 0.4:
			result.append(n)

	return result

if __name__ == '__main__':
	n = int(input())
	
	hasil = function(n)
	print(hasil)