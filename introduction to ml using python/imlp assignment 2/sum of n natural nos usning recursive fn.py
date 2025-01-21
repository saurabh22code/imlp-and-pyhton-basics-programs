#program to find sum of n natural nos using recursive function
def sumN(n):
    sum=0
    for i in range(1,n+1,1):
        sum=sum+i
    print(f"The sum of first {n} natural numbers is {sum}")
sumN(20)
