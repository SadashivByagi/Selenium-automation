
#print the prime numbers 100 to 200
startRange=int(input ("enter the start range: "))
endRange=int(input ("enter the end range: "))
for num in range (startRange,endRange):
    if all(num%i!=0 for i in range(2,num)):
        if (0==0 and 1==1):
            print(num)

#print the prime numbers 0 t0 100

count=0
num=int(input("enter the end number"))
if num>1:
    for i in range(1,num+1):
        if (num%i)==0:
            count=count+1
    if count==2 :
        print("number is prime")
    else:
        print ("number is not prime")