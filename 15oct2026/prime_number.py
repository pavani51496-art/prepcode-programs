number=int(input("enter a number:"))
flag=True
for i in range(2,number):
    if number%i==0:
        flag=False
if flag==true:
    print("print number")   
else:
    print("not prime")    
