"""
    *
   ***
  *****
 *******
*********
    """
for i in range(1,9,2):
    for s in range(4,1,-1):
        print(" ",end="")
    for x in range(1,i+1): #for printing each row
        print("*",end="") #pattern print
    print("\n")#changes the line