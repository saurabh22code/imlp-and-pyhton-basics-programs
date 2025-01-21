#question 1: check if a numb er is odd or even 
x=int(input("enter a number to check whether it is even or odd: "))
if x%2==0:
    print(f"The number {x} is even.")
elif x%2>0:
    print(f"the number {x} is odd.")
else:
    print("There is an error while input")
    
    
#question 2: program to print natural no.
n=int(input("enter the no. till which you want to print natural nos."))
for i in range(1,n+1,1):
    print(i,end="")
    if i==n:
        pass
    else:
        print(",",end="")
print("\n")   
     
#question 3: check prime number:
p=int(input("enter a number to check whether it is prime or not: "))
s=0
for i in range(1,p+1):
    if p%i==0:
        s+=1
    else:
        pass
    
if s==2:
    print(f"the number {p} is a prime number.")
elif s>2:
    print(f"the number {p} is not a prime number.")
else:
    pass


