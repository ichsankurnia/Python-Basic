"""
Welcome in Python
"""
import math
print(10)
a = 5
c = 4
print(a+c)
print(max(a,10,c,100))
print(min(a,c,0.24,0.1000))
print(round(6,25))

print()
print(math.cos(0))
print(str(math.pi) + " " + str(math.e)) #kalau di java & C# println/WriteLine(math.pi +" "+ math.e) tanpa harus di convert menjadi string dahulu
print(math.pi," ",math.e) #java & C# ("angka " + 10 + " dan " + 20)
b="5.5"
print(10+float(b))

print(2**3, 2**3., 2.**3, 2.**3.) 	# 8 8.0 8.0 8.0
print(6/3, 6/3., 6./3, 6./3.)		# 2.0 2.0 2.0 2.0
print(6//3, 6//3., 6.//3, 6.//3.)	# 2 2.0 2.0 2.0
print(6//4, 6.//4)					# 1 1.0
print(-6//4, 6.//-4)				# -2 -2.0
print(14%4, 12%4.5)					# 2 3.0
print(+2, -1.1, -4+4, -4.+8, -4-4, 4.-8)	# 2 -1.1 0 4.0 -8 -4.0
print(2**2**3, 2*3%5)				# 256, 1
print(25%13, 10% 15)				# 12 10
print(21.5326565656//2)				# 10.0

print("Section 2 Summary")

# Section 2 Summary
print((2 ** 4), (2 * 4.), (2 * 4)) 				# 16 8.0 8
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))	# -0.5 0.5 0 -1
print((2 % -4), (2 % 4), (2 ** 3 ** 2))			# -2 2 512