""" ============================ No 1 =============================
1. Maximum difference between two elements such that larger element appears after the smaller number
Given an array arr[] of integers, find out the maximum difference between any two elements
such that larger element appears after the smaller number.
Input : arr = {2, 3, 10, 6, 4, 8, 1}
Output : 8
Input : arr = {7, 9, 5, 8, 3, 2}
Output : 3
Hint:
1st sample: max is 10 - 2 = 8
2nd sample: max is 8 - 5 = 3
"""

def maxDiff(arr, size): 
    max_diff = arr[1] - arr[0]

    # maxx_diff = 1 8 4 2 6 -1
    for i in range(0, size): 
    	print("i", i)
    	for j in range(i+1, size):
    		print("j", j)
    		if arr[j] - arr[i] > max_diff:
    			print("max_diff awal", max_diff)
    			max_diff = arr[j] - arr[i]
    			print("max_diff hasil", max_diff)
    		else:
    			print("max_diff tidak berubah, karna hasil arr[{}]-arr[{}] = {} sama/lebih kecil dari max_diff sekarang ({})".format(j, i, arr[j]-arr[i], max_diff))
    		
      
    return max_diff 
      

# arr = [2, 3, 10, 6, 4, 8, 1]
arr = [7, 9, 5, 8, 3, 2]
# arr = [1, 2, 90, 10, 110]
print ("Maximum difference :", maxDiff(arr, len(arr)))


""" ========================= No 2 ==========================="""
"""
2.Longest prefix which is also suffix
Given a string s, find length of the longest prefix which is also suffix. The prefix and suffix should not
overlap.

Input : aabcdaabc
Output : 4

Input : abcab
Output : 2

Input : aaaa
Output : 2

Hint:
1st sample: prefix=suffix=aabc
"""
def longestPrefixSuffix(s) : 
    n = len(s) 
      
    for res in range(n // 2, 0, -1) : 
        prefix = s[0: res] 
        suffix = s[n - res: n] 
          
        if (prefix == suffix) : 
            return res 
    return 0
      
s = "blablabla"
print(longestPrefixSuffix(s)) 


"""
3. Compress string
Given a string s, that may contain repetitive characters, implement the function to modify and return the
input string,
such that each character once, along with the count of consecutive occurrence.
Do not append count if the character occurs only once.

input – aaaaabbbbcccccccdaa
OutPut – a5b4c7da2
"""
# def compression(string):
#     string = string.lower()
#     freq_count = {}

#     # 0, a
#     for index, char in enumerate(string):
#     	print(index, char)
#     	if char not in freq_count:
#     		freq_count[char] = 1 	# 'a' : 1
#     	else:
#     	    freq_count[char] += 1
#     	print(freq_count)

#     return_string = ''

#     for key, val in freq_count.items():
#     	return_string += key + str(val)

#     # for key in freq_count:
#     #     return_string += key + str(freq_count[key])

#     print(return_string)

#     return return_string

# compression(input("masukan string="))

# string = "aaaaabbbbcccccccdaa"
# result_string = ""

# i = 0
# while( i < len(string) - 1) : 

#     count = 1
#     while string[i] == string[i+1] : 

#         i += 1
#         count += 1
          
#         if i + 1 == len(string): 
#             break

#     print(str(string[i]) + str(count)) 

#     result_string += str(string[i]) + str(count)
#     i += 1
#     return result_string



def main(string):
	result_string = ""

	i = 0
	while i < len(string):
		count = 1
		while string[i] == string[i+1]:
			i += 1
			count += 1
			if i+1 == len(string):
				break

		# print(string[i]+str(count))

		result_string += str(string[i]) + str(count)
		# print(result_string)
		i += 1

	return result_string

if __name__ == '__main__':
	
	result = main("aaaaabbbbcccccccdaa")
	print(result)

"""
4.Binary gap
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded
by ones at both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4
and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps.
The number 32 has binary representation 100000 and has no binary gaps.
Write a function, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.
For example, given N = 1041 the function should return 5,
because N has binary representation 10000010001 and so its longest binary gap is of length 5.
Given N = 32 the function should return 0, because N has binary representation '100000' and thus no
binary gaps.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..2,147,483,647].

4. kesenjangan Biner
Celah biner dalam bilangan bulat positif N adalah setiap urutan maksimal dari nol berurutan yang dikelilingi
oleh yang di kedua ujungnya dalam representasi biner dari N.
Misalnya, nomor 9 memiliki representasi biner 1001 dan berisi celah biner dengan panjang 2.
Angka 529 memiliki representasi biner 1000010001 dan berisi dua celah biner: satu dengan panjang 4
dan satu dengan panjang 3.
Angka 20 memiliki representasi biner 10100 dan berisi satu celah biner dengan panjang 1.
Angka 15 memiliki representasi biner 1111 dan tidak memiliki celah biner.
Angka 32 memiliki representasi biner 100000 dan tidak memiliki celah biner.
Tulis fungsi, diberi bilangan bulat positif N, mengembalikan panjang celah biner terpanjangnya.
Fungsi harus mengembalikan 0 jika N tidak mengandung celah biner.
Misalnya, mengingat N = 1041 fungsi harus mengembalikan 5,
karena N memiliki representasi biner 10000010001 dan jadi celah biner terpanjangnya adalah panjang 5.
Diberikan N = 32 fungsi harus mengembalikan 0, karena N memiliki representasi biner '100000' dan dengan demikian tidak
kesenjangan biner.
Tulis algoritma yang efisien untuk asumsi-asumsi berikut:
N adalah bilangan bulat dalam kisaran [1..2,147.483.647]
"""

def dectobin(num):
	return bin(num).replace("0b", "")

def main():
	n = 0

	for i in range(len(biner)):
		n += 1
		try:
			if biner[0] == biner[i+1]:
				break
		except:
			n = 1

	return n-1

if __name__ == '__main__':
	num = int(input("input a decimal number: "))
	biner = dectobin(num)
	print(biner)
	print(main())



"""
5. Self-numbers.
For any positive integer n, define d(n) to be n plus the sum of the digits of n.
For example, d(75) = 75 + 7 + 5 = 87.
The number n is called a generator of d(n).
Some numbers have more than one generator: for example, 101 has two generators, 91 and 100.
91 + 9 + 1 = 101
100 + 1 + 0 + 0 = 101
A number with no generators is a self-number.
There are thirteen self-numbers less than 100: 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, and 97.
So the sum of all self-numbers which are bigger than 0 and smaller than 100 is 493
What is the sum of all self-numbers which are bigger than 0 and smaller than 5000?
Please write your solution using your preferred programming language.

5. Angka sendiri.
Untuk bilangan bulat positif n, tentukan d (n) sebagai n ditambah jumlah digit n.
Misalnya, d (75) = 75 + 7 + 5 = 87.
Angka n disebut generator dari d (n).
Beberapa angka memiliki lebih dari satu generator: misalnya, 101 memiliki dua generator, 91 dan 100.
91 + 9 + 1 = 101
100 + 1 + 0 + 0 = 101
Nomor tanpa generator adalah nomor mandiri.
Ada tiga belas angka mandiri kurang dari 100: 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 75, 86, dan 97.
Jadi jumlah semua bilangan mandiri yang lebih besar dari 0 dan lebih kecil dari 100 adalah 493
Berapa jumlah semua nomor mandiri yang lebih besar dari 0 dan lebih kecil dari 5000?
Silakan tulis solusi Anda menggunakan bahasa pemrograman pilihan Anda.

"""

def self_number():
    li = []
    for i in range(1,5001):
        li.append(i + sum([int(j) for j in str(i)]))

    return sum(set(range(1,5001)) - set(li))

print(self_number())

# sum(set(range(1, 5000)) - {x + sum([int(a) for a in str(x)]) for x in range(1, 5000)})