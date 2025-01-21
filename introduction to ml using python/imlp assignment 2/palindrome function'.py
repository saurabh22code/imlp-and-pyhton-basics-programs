#create a function to check whether a number is palindrome or not
def ispalindrome(x):
    num=x
    temp = num
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    if num == reverse:
        print(f'{x} is a plaindrome number')
    else:
        print(f"{x} is Not a Palindrome number")

x=int(input("enter a numbe rto check whether a number is palindrome or not: "))
ispalindrome(x)