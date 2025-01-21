# create a program to count the no of characters in a string and store them in a dictionary

#taking input of string to count the characters in that string
x=str(input("enter the string to count the characters: "))

#counting the characters
c=len(x)

#storing them in a dictionary
d={x:c}

#printing the dictionary in which the values are stored
print(d)
