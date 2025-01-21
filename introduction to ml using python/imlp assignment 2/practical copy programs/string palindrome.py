#program to check astring is palindrom or not
x=input("Enter a string: ")
list=list(x)
list.reverse()
s=""
for i in list:
    s+=i
if x==s:
    print("Original String: ",x)
    print("Reversed String: ",s)
    print("The given string is palindrome.")
else:
    print("Original String: ",x)
    print("Reversed String: ",s)
    print("The given string is not palindrome.")