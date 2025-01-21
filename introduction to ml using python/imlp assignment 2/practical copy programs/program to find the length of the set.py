#program to find the length of the set
set_1=set()
#taking input for set 1
x=int(input("Enter The elements you want to add in first set: "))
for i in range(1,x+1):
    element=int(input("Enter The element:"))
    set_1.add(element)
list=[]
for i in set_1:
    list.append(i)
    
print("The length of the set is:",len(list))