mylist=[("x",1),("Y",2),("Z",3),"S"]
mylist=list(dict.fromkeys(mylist))
print(mylist)

mylist=tuple(mylist)
print(mylist)


#Converting list of tuples to dictionary by using dict() constructor
color=[('red',1),('blue',2),('green',3)]
d=dict(color)
print (d)#Output:{'red': 1, 'blue': 2, 'green': 3}

mylist1=[("x",1),("Y",2),("Z",3),("S",2)]
d1=dict(mylist1)
print(d1)

mylist2=[(1,2),(3,4),(5,6),(7,8)]
d2=dict(mylist2)
print(d2)



#remove the duplicate from the list

mylist3=[1,2,3,4,5,6,7,8,9,10,10,1,2,3,4,5]
mynewlist=[]
for i in mylist3:
    if i not in mynewlist:
        mynewlist.append(i)
print(mynewlist)


newlist=[i for i in range (1,1000)]
mystring="Sadashiv"
print(newlist)
print(mystring)


#map function in python

def add_func(n):
    return n*3

num=(1,2,3,4,5,6)
result=map(add_func,num)
print(list(result))

#find the factorial of the number
num2=0
factorial=1
if num2<2:
    print("factorial of the given number is 1",factorial)
for i in range (1, num2+1):
    factorial=factorial*i
print(factorial)



print (bool())

