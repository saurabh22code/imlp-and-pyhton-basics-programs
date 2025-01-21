"""WAP in python to create a file student and store the following information:
Roll  Name  Marks
1	Ram	    40
2 	John     52
"""

x=open("student.txt","w")
x.write( "Roll  Name  Marks")
x.write("\n1	Ram	    40")
x.write("\n2 	John     52")
x.close()