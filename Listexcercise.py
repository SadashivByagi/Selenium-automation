list1=[1,2,3,4,4,5,6,7]
list2=[1,2,3,45,6,7,8,9]

#list1.extend(list2)
print(list1)
mynewlist=[]
for i in list1:
    if i not in mynewlist:
        mynewlist.append(i)
print(mynewlist)

mylist2= list1 + list2
print(mylist2)

mytuple1=(1,2,3,4)
mytuple2=(4,5,6,7)
mytuple=mytuple1 + mytuple2
print(mytuple)



