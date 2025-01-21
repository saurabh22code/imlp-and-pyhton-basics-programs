
"""

Q.8. . Create a python programme to modify the content of the given text file

Here’s a Python program to modify the content of a given text file. The program reads the content of the file, applies changes (e.g., replacing words), and writes the modified content back to the file:"""
def modify_file_content(file_name, old_text, new_text):
    try:
        # Step 1: Read the content of the file
        with open(file_name, "r") as file:
            content = file.read()

        # Step 2: Modify the content by replacing the specified text
        modified_content = content.replace(old_text, new_text)

        # Step 3: Write the modified content back to the file
        with open(file_name, "w") as file:
            file.write(modified_content)

        print(f"The file '{file_name}' has been modified successfully.")
        print(f"Replaced '{old_text}' with '{new_text}'.")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_name = "example.txt"  # Replace with the name of your text file
old_text = "old_word"      # Replace with the word you want to replace
new_text = "new_word"      # Replace with the new word

modify_file_content(file_name, old_text, new_text)
