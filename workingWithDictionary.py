d={"Suresh":566,"Ramesh":567,"Kishore":568}
Dict_keys1=input("Enter the key")
if Dict_keys1 in d:
    print("key exist",Dict_keys1)
    print("Key Value ",d[Dict_keys1])
else:
    print("Key doesn't exist")
Dict_k=d.keys()
print(Dict_k)

#Concatanation of two dictionarys
dict1={"Name":"Sadashiv", "Lastname":"Byagi","Country":"UK","Address":"Southampton"}
dict2={"Name1":"Bharati","Lastname1":"Devaramani","Country1":"USA","Address":"Cambridge"}
dict1.update(dict2)
print (dict1)



