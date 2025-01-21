#5.	Create a program that counts the occurrences of each character in a string and prints the results
x=input("Enter a string: ")
s=list(x)
n=[]
for a in s:
    if a not in n:
        print(f"The occurence of '{a}' is {s.count(a)}")
        n.append(a)