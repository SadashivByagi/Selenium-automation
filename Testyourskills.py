# fibonacci series
a = 0
b = 1
num = int(input("enter the input number to generate fibonacci series"))
print(a)
print(b)

for i in range(2, num):
    c = a + b
    a = b
    b = c
    print(c)

# print the prime numbers from 100 to 200

# catch I will have to consider

Start_number = int(input("Enter the start number"))
end_number = int(input("Enter the end number"))

for j in range(Start_number, end_number):
    if (j % k != 0 for k in range(2, j)):
        print(j)

# factorail of the given number
factorial = 1
num = int(input("enter the input number"))

if num < 0:
    print("Factorial doesn't exist for negative number")
elif (num == 1):
    print("Factorial of the number ia 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial)

# string reverse in python

string = "I am learning python"
result = ""
for i in string:
    result = i + result
print(result)
realstring = ("".join(reversed(result)))
print(realstring)
# other method using string slicing

revers = realstring[::-1]
print(revers)

# list reverse
mylist = [1, 2, 3, 4, 5, 6]
mylist.reverse()

print(mylist)
print(mylist[::-1])

# reverse the list using for loop
mylist2 = [2, 3, 4, 5, 6, 7, 8, 9]
mynew_list = []

for i in range(len(mylist2) - 1, -1, -1):
    mynew_list.append(mylist2[i])
print(mynew_list)

a = [100, 200, 72, 78, 54, 1000]
a.sort()
print(a)

# sort the list without using sort


li = [1, 2, 3, 4, 5, 6, 7, 8]


def rev(lis):
    print("list reverse within function")
    return lis[::-1]


print(rev(li))

# find the duplicates from the given list
duplicate_elements = []
newList = [1, 2, 3, 4, 5, 5, 4]
for x in newList:
    if newList.count(x) > 1:
        duplicate_elements.append(newList[x])
print(duplicate_elements)

d = set(newList)
d.union()
print(d)
d.intersection()
print(d)

# Find the digit from the string
newstr = ""
mystr = "123gaspoo890"
a = filter(str.isdigit, mystr)
string_filter = "".join(a)
print(string_filter)

# remove the repetitive characters

strngs="sadashiv"
newstring=""
for char in strngs:
    if char not in newstring:
        newstring=newstring+char
print(newstring)


