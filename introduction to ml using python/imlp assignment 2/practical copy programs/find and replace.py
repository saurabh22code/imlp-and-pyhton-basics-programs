#4.	Write a Python script that finds and replaces a specific substring within a string entered by the user.
x=input("enter a string: ")
st1=input("Enter the string want to replace: ")
st2=input("Enter the string you want to replace with: ")
list=x.split()
for i in range(0,len(list)):
    if list[i]==st1:
        list.remove(list[i])
        list.insert(i,st2)
s=""
for i in list:
    s+=i
    s+=" "
    
print(s)