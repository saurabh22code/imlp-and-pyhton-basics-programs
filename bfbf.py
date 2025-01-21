def upton(n):
    if n==1:
        return 1
    else:
        return (1/n)+upton(n-1)
x=upton(10)
print(x)