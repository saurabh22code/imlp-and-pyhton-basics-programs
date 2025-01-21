#.	Write a Python program to sum all the items in a list.
s=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in range(0,len(s)):
    sum+=s[i]
    
print("sum of all elements: ",sum)