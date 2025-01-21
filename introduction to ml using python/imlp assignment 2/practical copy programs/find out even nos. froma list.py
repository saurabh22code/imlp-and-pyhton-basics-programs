#7.	Write a Python program to select the even items of a list.
list_1=[12,32,5,66,88,9,23]
even=[]
for i in range(0,len(list_1)):
    if list_1[i]%2==0:
        even.append(list_1[i])
print(f"{even} are the even no. present in list.")