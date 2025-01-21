#program to calculate the following using match function
print("1.add\n2.subtract\n3.multiply\n4.divide\n5.exponent")
choice=int(input("enter your choice: "))
num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
match choice:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1*num2)
    case 5:
        print(num1**num2)
    
    