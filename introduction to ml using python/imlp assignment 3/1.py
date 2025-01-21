"""
Q.1 What is a file and its operations?
A file in Python is a container on a storage device that holds data, such as text or binary information. Files are used to store data permanently so that it can be accessed and processed later.
File Operations in Python
Here are the common file operations in Python:
1.	Opening a File
o	Use the open() function to open a file.
o	Syntax: open(file_name, mode)
o	Modes: 
	'r' - Read (default)
	'w' - Write (overwrites file if exists, creates new if not)
	'a' - Append (adds data to the end)
	'b' - Binary mode
	'+' - Read and Write
2.	Reading a File
o	Methods: 
	read() - Reads the entire file or a specified number of characters.
	readline() - Reads a single line from the file.
	readlines() - Reads all lines as a list of strings.
3.	Writing to a File
o	Methods: 
	write() - Writes a string to the file.
	writelines() - Writes a list of strings to the file.
4.	Closing a File
o	Use the close() method to close the file and free system resources.
o	Example: file.close()
5.	Using with Statement
o	Ensures that the file is properly closed after its operations are completed.
o	Example: 
o	with open("file.txt", "r") as file:
o	    content = file.read()
6.	Other Operations
o	tell() - Returns the current file pointer position.
o	seek(offset) - Moves the file pointer to a specific position.
o	flush() - Flushes the internal buffer to the file."""
#Example:
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, Python!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
