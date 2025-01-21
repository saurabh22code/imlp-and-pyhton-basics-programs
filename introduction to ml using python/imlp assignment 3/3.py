'''Q.3. create a program in python which reads a text file named "input.txt" and count the total number of words in the file'''

# Program to count the total number of words in a file 
try:
    # Open the file in read mode
    with open("input.txt", "r") as file:
        # Read the entire content of the file
        content = file.read()
        
        # Split the content into words using whitespace as a delimiter
        words = content.split()
        
        # Count the total number of words
        word_count = len(words)
        
        # Display the word count
        print(f"Total number of words in 'input.txt': {word_count}")
except FileNotFoundError:
    print("The file 'input.txt' was not found. Please make sure it exists in the same directory.")
except Exception as e:
    print(f"An error occurred: {e}")
