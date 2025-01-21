def fibonacci(n):
    x1=0
    x2=1
    x3=0
    for i in range(0,n+1,1):
        print(x3)
        x1,x2=x2,x3
        x3=x1+x2

fibonacci(22)