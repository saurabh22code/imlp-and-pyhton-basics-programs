f=open('first.txt','w+')
f.write("""File Handling
File:to store data in a computer we use file
#there are two types of file in python
1.text file
2.binary file

#Advantages of using file
There are four advantages of storing in a file
1.When the data is store in a file it is stored permanently
2.It is possible to update the file data
	Ex. we can add new data to a existing file, modify the existing data from file and delete the unnecessary data from the file
3.once the data is stored in file the same data can be shared by various programmes
4.files are highly useful to store huge amount of data

#python code to open file
f=open(“first.txt”,”w”)
f.write(“welcome to AJU”)
f.close()
#file opening modes
1.	r:- to read data from a file
2.	a:-to append data to a file we use this
3.	w+:-to write an read data of a file we use w+
note: the previous data in the file will be deleted
4.	r+:-to read and write data of a file we use this file mode
note: The previous data in the file will not be deleted
     5.a+: to append and read data of a file we use this

""")
f.close()
