def sumn(n):
    
    if n==0 or n==1:
        return 1
    else:
        return n+sumn(n-1)
n=int(input("Enter a number: "))
print(f"the sum of {n} is ",sumn(n))