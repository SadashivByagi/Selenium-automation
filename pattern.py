# # # #
# # # #
# # # #
# # # #

'''*****
   *****
   *****
   *****
   *****'''

for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()


for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()

print("This is another format")

for i in range(5,0,-1):
    for j in range (i,0,-1):
        print("*", end=" ")
    print()
