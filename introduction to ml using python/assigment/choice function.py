"""
Create a program to calculate the following using the match expression
a. Addition of two numbers
b. Subtraction of two numbers
c. Multiplication of two numbers
d. Division of two numbers
e. Exponent of two numbers

"""
#printing the list to choose the operation the user wants to do
print("a.Addition\nb.Subtraction\nc.Multiplication\nd.Division\ne.Exponent")

#taking input for operation from user
choice=str(input("Enter your choice: "))

#taking input of two numbers to perform operations on them as per the choice
number_1=int(input("Enter first number: "))
number_2=int(input("Enter second number: "))

#performing operations as per the choice
match choice:
    case "a":
        print(f"The sum of {number_1} and {number_2} is {number_1+number_2}")
    case "b":
        print(f"The subtraction of {number_1} and {number_2} is {number_1 - number_2}")
    case "c":
        print(f"The multiplication of {number_1} and {number_2} is {number_1*number_2}")
    case "d":
        print(f"The division of {number_1} and {number_2} is {number_1/number_2}")
    case"e":
        print(f"The exponent of {number_1} and {number_2} is {number_1**number_2}")
    case _:
        print("invalid input")
