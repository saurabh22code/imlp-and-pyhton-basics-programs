#program to create a function to check whether a number is prime or not
def checkprime(x):
    factors=0
    for i in range(1,x+1,1):
        if x%i==0:
            factors+=1
        else:
            pass
    if factors>2:
        print(f"{x} is not a prime number.")
    else:
        print(f"{x} is a prime number")
x=int(input("enter a number to check whether it is prime or not: "))
checkprime(x)