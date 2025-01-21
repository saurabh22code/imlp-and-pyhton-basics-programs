a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
x=input("enter your operator choice: ")
if x=="+":
    print(a+b)
elif x=="-":
    print(a-b)
elif x=="*":
    print(a*b)
elif x=="/":
    print(a/b)
else:
    print("Invalid input")