#program to create a function which print fibonacci series upto n numbers
def fibonacciupton(n):
    n1,n2=0,1
    nth=0
    print(n1)
    for i in range(0,n+1,1):
        nth=n1+n2
        n1=n2
        n2=nth
        print(nth)
x=int(input("enter the value of n:"))
fibonacciupton(x)