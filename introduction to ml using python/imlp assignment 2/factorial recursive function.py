#program to create a recurcive function to print fact of a number 
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)   
    
# take input from the user  
num = int(input("Enter a number: "))  
# check is the number is negative  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",fact(num))  