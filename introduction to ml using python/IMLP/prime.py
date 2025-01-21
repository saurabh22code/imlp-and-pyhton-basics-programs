n=int(input("Enter a no.: "))
s=0
for i in range(1,n+1):
    x=n%i
    if x==0:
        s+=1
    elif x>0:
        print(end="")
if s>2:
    print(n,"is not a prime no.")
else:
    print(n,"is a prime no.")
