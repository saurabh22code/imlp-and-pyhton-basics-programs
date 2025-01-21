file=open("example.txt","r")
file.seek(7)
print(file.read(5))
file.close()
