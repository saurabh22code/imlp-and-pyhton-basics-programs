# create a program to add digits of a number

#taking input from user for the number to add their digits
number=int(input("enter the number: "))

#taking A blank variable to add the digits in that
sum_of_digits=0

#process to find their digits and adding them in variable above
for i in str(number):
    sum_of_digits+=int(i)

#printing the sum of digits of the number given by the user
print(f"The sum of digits of {number} is {sum_of_digits}")