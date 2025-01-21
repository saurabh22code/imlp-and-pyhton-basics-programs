#2.	Write a Python program to multiplies all the items in a list.
s=[1,2,3,4,5]
sum=1
for i in range(0,len(s)):
    sum*=s[i]
print("multiply of all elements: ",sum)