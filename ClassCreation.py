import numpy as np


class employee():
    def __init__(sada,name,ID,phone, address):
        sada.name=name
        sada.ID=ID
        sada.phone=phone
        sada.address=address


    def employee1(sada):
        print("Create the employee1 details :" +  sada.name)
        print("update the ID :", sada.ID)
        print("update the phone :", sada.phone)
        print("update the address details :"+ sada.address)


a= employee("sadashiv",351372,9731525224,"Southampton")
a.employee1()

n1=np.zeros((5,5))
print(n1)


