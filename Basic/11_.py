def fib(n):
    a, b = 0 , 1  # a=0, b=1
    while a < n:
        print(a, end=" ") #end itu fungsinya buat geser ke samping
        a, b = b, a+b
    print()

def loop(a):
    for x in range(0,a):
        print(x)
    return x

def hit(a,b,c):
    z = a + b + c
    return z

def text(mutia):
    print(mutia)

def fungsi(sha):
    return sha

fib(1000)
loop(10)
print(hit(90,34,78)) #method return
text("mffjlnsjksnfknj")
print(fungsi(80986))
