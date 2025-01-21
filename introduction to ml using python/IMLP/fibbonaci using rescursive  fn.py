def fibbonacire(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbonacire(n-1)+fibbonacire(n-2)
n=int(input("enter the number:"))
for i in range(1,n+1):
    print(fibbonacire(i))