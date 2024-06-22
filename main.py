# Simple Python Program to determine whether a given integer is Prime 
integer = 9
if integer > 1:
    for i in range (2,(integer//2)+1):
        if (integer%i)==0:
          print("The integer is not a prime !")
        else:
          print("The integer is  a prime !")
          break
else:
    print("The integer is not a not prime !")  
