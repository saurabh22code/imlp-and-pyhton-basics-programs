#write a program in python to find the largest no. among three no.
a=int(input("enter 1st no.:"))
b=int(input("enter 2nd no.:"))
c=int(input("enter 3rd no.:"))
if a>b:
    if a>c:
        print(a,"is the graetest among all of them.")
    else:
        print(c,"is the greatest among all of them.")
elif b>c:
    if b>a:
        print(b,"is the greatest among all of them.")
    else:
        print(a,"is the greatest among all of them.")
else:
    if c>a:
        print(c,"is the greatest among all of them.")
    else:
        print(a,"is the greatest among all of them.")
