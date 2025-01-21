#program to check the garde of student through their marks
while True:
    mark=float(input("ENTER MARKS: "))
    if mark<70:
        print("Garde A")
    elif mark<=80:
        print("Grade A+")
    else:
        print("invalid marks")
