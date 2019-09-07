# def function(kata):

# 	kata = kata[:len(kata)-2]
	
# 	return kata

def function(kata):

    s = set()
    string = []

    for char in kata:
        if char not in s:
            s.add(char)
            string.append(char)

    return ''.join(string)


if __name__ == '__main__':
	kata = input().upper()
	
	hasil = function(kata)
	print(hasil)