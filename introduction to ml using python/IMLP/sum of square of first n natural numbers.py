#Programme to find sum of square first n natural nos.
n=int(input('Enter a number: '))
s=0
for i in range(1, n + 1):
    s+= i * i
print("Sum=",s)