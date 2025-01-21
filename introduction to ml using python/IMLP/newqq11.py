def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    # Reverse the string
    reversed_num_str = num_str[::-1]
    # Check if the original string is equal to the reversed string
    return num_str == reversed_num_str


# Example usage
number=int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
