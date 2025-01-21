'''
Q.4. create the python program that creates a text file named "emaildata.txt" and extract all the email addresses present in the file using regular expression module

Here's a Python program that creates a text file named emaildata.txt, writes sample text with email addresses to it, and then extracts all email addresses using the re (regular expression) module:

'''
import re

# Step 1: Create a text file named 'emaildata.txt' with sample content
sample_content = """
Welcome to the email extraction test.
Here are some email addresses:
example1@gmail.com, contact_us@domain.org, user.name@company.com
For queries, email us at info@website.net or support@helpdesk.co.
"""

# Write the sample content to 'emaildata.txt'
with open("emaildata.txt", "w") as file:
    file.write(sample_content)

print("File 'emaildata.txt' created successfully!")

# Step 2: Extract email addresses from the file
try:
    # Open the file in read mode
    with open("emaildata.txt", "r") as file:
        content = file.read()
    
    # Regular expression to match email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all email addresses in the content
    email_addresses = re.findall(email_pattern, content)
    
    # Print the extracted email addresses
    print("Extracted Email Addresses:")
    for email in email_addresses:
        print(email)
except FileNotFoundError:
    print("The file 'emaildata.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
