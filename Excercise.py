class myClass():
    pass

o1=myClass()
o2=myClass()

print (type(o1))
print(type(o2))

o1.x=20
o1.y=[10,20,30]

print (vars(o1))

o2.a={1,2,3,4}
o2.b={"a":1,"b":4,"c":28}

print (vars(o2))



