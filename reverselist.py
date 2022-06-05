def listReverse(myList):
    newlist=[]
    for i in range(len(myList)-1,-1,-1):
        newlist.append(myList[i])
    print(newlist)

listReverse([1,2,3,4,45,6,7,8,9])

#find the length of the given string

def LengthofString(mystring4):
    count=0
    for i in mystring4:
        count=count+1
    print(count)

LengthofString("Sadashiv")

#find palindrome or not
def palindrome(palindromeStr):
    rev=("".join(reversed(palindromeStr)))
    if (rev==palindromeStr):
        return True
        return False

print (palindrome("madam"))

mystring6="madam1"
print(mystring6[::-1])

def StringRevr(Mystr):
    result=""
    for i in Mystr:
        result=i+result
    print(result)

StringRevr("Sadashiv")

#print the fibonacci series
num=int(input("enter the number to generate fibonacci series"))
a=0
b=1
print(a)
print(b)
for i in range (2,num):
    c=a+b
    a=b
    b=c
    print(c)


#print the list of duplicates from the list

li=[1,2,7,4,5,6,7,7,8,8]
for i in li:
    if (li.count(i)>1):
        print("duplicate", (i))
    else:
        print("No duplicate", (i))







