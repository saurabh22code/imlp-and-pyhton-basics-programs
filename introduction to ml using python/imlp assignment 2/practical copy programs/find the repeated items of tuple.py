tuple=(12,34,12,23,23,34,45,45,65,45)
s=[]
for i in range(0,len(tuple)):
    if tuple[i] not in s:
        if tuple.count(tuple[i])>1:
            s.append(tuple[i])
print(s,"are repeated item in the tuple given.")