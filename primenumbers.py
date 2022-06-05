
#prime number
number=0
n=10
for i in range(1,n):
    if n%i==0:
        number=number+1
if number==2:
    print(n," is prime number")
else:
    print(n,"is not prime number")

#fibonacci series
a=0
b=1
num=10
print(a)
print(b)
for i in range (2,num):
    c=a+b
    a=b
    b=c
    print(c)

#factorial of the numbers
num=10
factorial=1
if num<0:
    print("Factorial doesn't exist for negative numbers")
elif (num==1):
    print("Factorial is 1")
else:
    for i in range (1,num+1 ):
        factorial=factorial*i
    print("The factorial of the number is", factorial)

num10=12
num2=76
num3=76
if (num10>num2):
    print("biggest number",num10)
elif (num2>num3):
    print("biggest number2",num2)
else:
    print("biggest number3",num3)

#palindrome
mystring="gadag1"
result=""
for i in mystring:
    result=i+result
print(result)
if result==mystring:
    print("the given string is palindrome")
else:
    print("The given string is not palindrome")

#string reverse
reversestr1="sadashiv1"
result=""
for j in reversestr1:
    result=j+result
print(result)

reversestr="sadashiv"
print("".join(reversed(reversestr)))

reversestr="sadashiv"
print(reversestr[::-1])

#find the length of the given string
findlen="Sadashiv"
count=0
for i in findlen:
    count=count+1
print(count)


print(len(findlen))

#program tpo reverse the list

mylist=[1,2,3,4,5,6,78]
mynewlist1=[]
for i in range (len(mylist)-1,-1,-1):
    mynewlist1.append(mylist[i])
print(mynewlist1)


