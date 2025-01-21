#6.	Write a Python program to find common items from two lists
list_1=[12,33,56,67,"apple"]
list_2=[43,45,67,78,"apple"]
common=[]
for i in range(0,len(list_1)):
    for s in range(0,len(list_2)):
        if list_1[i]==list_2[s]:
            common.append(list_1[i])
            
print(f"{common} is common in both list.")
        