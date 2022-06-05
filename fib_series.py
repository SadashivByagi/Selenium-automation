def fibo(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range (2,n):
        c=a+b
        a=b
        b=c
        print(c)

fibo(8)

#program to reverse the string

def strReverse(myStr):
    result = ""
    for i in myStr:
        result = i + result
    return (result)

a=strReverse("python")
print(a)

#fibonacci series
def fibonacci(n1):
    d = 0
    e = 1
    print(d)
    print(e)
    for i in range(2, n1):
        f = d + e
        d = e
        e = f
        print(e)

fibonacci(10)

#program to find the given number is prime or not





