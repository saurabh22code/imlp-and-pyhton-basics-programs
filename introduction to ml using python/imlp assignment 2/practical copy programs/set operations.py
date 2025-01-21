#2.	Write a Python program to perform following operations on set: intersection of sets, union of sets, set difference, symmetric difference, clear a set
set_1=set()
set_2=set()
#taking input for set 1
x=int(input("Enter The elements you want to add in first set: "))
for i in range(1,x+1):
    element=int(input("Enter The element:"))
    set_1.add(element)

y=int(input("Enter The elements you want to add in first set: "))
for i in range(1,y+1):
    element=int(input("Enter The element:"))
    set_2.add(element)
print("""
1.Intersection of set 1 and set 2
2.Union of sets
3.Sets difference
4.Symmetric difference
5.clear a set
""")
choice=int(input("enter your choice: "))

print(set_1)
print(set_2)
if choice==1:
    print(f"The intersection of both The sets is below: \n{set_1.intersection(set_2)}") 
elif choice==2:
    print(f"Union of both The sets is below:\n{set_1.union(set_2)}")
elif choice==3:
    print(f"The difference of The sets is below:\n{set_1.difference(set_2)}")
elif choice==4:
    print(f"The symmetric difference of The sets is below:\n{set_1.symmetric_difference(set_2)}")
elif choice==5:
    print(f"The cleared set is below:\n{set_1.clear(),"\n",set_2.clear()}")
else:
    print("!!!Invalid choice!!!")

