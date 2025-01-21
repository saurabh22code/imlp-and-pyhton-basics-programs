#program to find the number of characters in a string given by user
x=input("Enter the string: ")
l=len(x)
for i in x:
    if i.isspace():
        l-=1
    else:
        pass
print("the number of characters in the string are: ",l)