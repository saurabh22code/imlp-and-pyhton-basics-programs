#program to print the following pattern
"""
123456
12345
1234
123
12
1
"""

#taking input for rows to print the pattern
x=int(input("enter the number of rows:"))

#opening a for loop to give a value in decreasing order to print the pattern
for i in range(x,0,-1):
    #further process for printing of pattern
    for j in range(1,i+1):
        print(j,end=" ")
    #printing a \n after printing a row of pattern to change the line
    print("\n")