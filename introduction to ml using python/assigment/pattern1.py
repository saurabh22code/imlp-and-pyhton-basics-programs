# program to print following pattern
"""
1
12
123
1234
12345
"""
#taking input for numbers of rows of pattern
x=int(input("enter the number of rows:"))

#opeing a for loop to give value in increasing order to print pattern
for i in range(1,x+1):
    #process to print the pattern
    for j in range(1,i+1):
        print(j,end=" ")
    #print \n to change the line after printing one row
    print("\n")