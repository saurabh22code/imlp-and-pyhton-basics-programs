print("""
    Pattern 1:
    1234567
    123456
    12345
    1234
    123
    12
    1
    """)

print("""
    Pattern 2:
    1
    12
    123
    1234
    12345
    123456
    1234567
      
      """)

print("""
    pattern 3:
            1
           12
          123
         1234
        12345
       123456  
      """)

#program to print pattern 1
n=int(input("enter the no. of rows of pattern: "))
choice=int(input("pattern 1 or 2 or 3: "))
def pattern1(n):
    for i in range(n,0,-1):
        for w in range(1,i+1,1):
            print(w,end="")
        print(end="\n")

def pattern2(n):
    for i in range(1,n+1,1):
        for x in range(1,i+1,1):
            print(x,end="")
        print(end="\n")
    
def pattern3(n):
    for i in range(1,n+1,1):
        for x in range(1,n-i+1,1):
            if i<10:
                print(" ",end="")
            elif i>9:
                print(" ",end="")
        for c in range(1,i+1,1):
            print(c,end="")
        print(end="\n")
        
if choice==1:
    pattern1(n)
elif choice==2:
    pattern2(n)
elif choice==3:
    pattern3(n)