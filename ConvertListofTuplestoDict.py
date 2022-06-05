from itertools import zip_longest

listofTuple=[("red",1),("green",2),("yellow",3)]
d= dict(listofTuple)
print(d)

#converting the two lists into a dictionary
l1=[1,2,3,4]
l2=["a","b","c","d"]
d1=zip(l1,l2)
print (d1)
d2=dict(d1)
print (d2)

#3.Converting Two Lists of Different Length to a Dictionary
l3=[1,2,3,4,5,6,7,8]
l4=["a","b","c","d","e"]
d3=zip(l3,l4)
d4=dict(d3)
print(d4)

#4,converting the two lists of different length to a dictionary with longest_zip keyword

l5=[1,2,3,4,5,6,7,8,9]
l6=["a","b","c","d","e"]
d5=zip_longest(l5,l6)
print(d5)
d6=dict(d5)
print(d6)

#4,converting the two lists of different length to a dictionary with longest_zip keyword

l5=[1,2,3,4,5,6,7,8,9]
l6=["a","b","c","d","e"]
d5=zip_longest(l5,l6,fillvalue="X")
print(d5)
d6=dict(d5)
print(d6)

#5 converting the list of alternative values into dictionary

l7=[1,"a",2,"b",3,"c",4,"d",5,"e"]
l8=l7[::2]
l9=l7[1::2]
z=zip(l8,l9)
d7=dict(z)
print(d7)

#converting list of dictionaries into a single dictionaries

l1=[{1:"a"},{2:"b"},{3:"c"}]
d1={}
for i in l1:
    d1.update(i)
print(d1)

#converting a list to a dictionary using dict.formkeys()

l1=["red","blue","orange"]
d1=dict.fromkeys(l1,"colors")
print(d1)
#converting a netsed list into dictionary

l9=[[1,2],[3,4],[4,[5,6]]]
d1={x[0]:x[1] for x in l9}
print (d1)











