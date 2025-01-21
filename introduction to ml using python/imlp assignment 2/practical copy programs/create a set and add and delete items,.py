#program to create a set and add memebers and delete an item form the set
s=set()
o=int(input("enter no. of elements you want to add: "))
for i in range(1,o+1):
    a=int(input("enter a number to add in set: "))
    s.add(a)
print(s)
d=input("do you want to remove any element from set(Y/N): ")
if d=="Y"or"y":
    f=int(input("which element you want to remove? :"))
    s.remove(f)
else:
    pass
print(s)   