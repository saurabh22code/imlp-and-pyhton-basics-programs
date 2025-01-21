def sumofcube(n):
    if n==0 or n==1:
        return 1
    else:
        return (n**3)+sumofcube(n-1)
n=int(input("Enter a number: "))
print(sumofcube(n))