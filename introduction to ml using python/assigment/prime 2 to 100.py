#program to print prime numbers between 2 and 100

#taking a range which gives number in increasing order
for n in range(2,101):
    #taking a temporary variable to store numbers of factor of the number
    s=0
    #finding factors for a number
    for i in range(1, n + 1):
        x = n % i
        if x == 0:
            s += 1
        elif x > 0:
            print(end="")
    #printing the prime numbers  whose factors are 1 and the number itself
    if s==2:
        print(n)

