s="00101000"
K=2
x=0
y=0

#code here
n=len(s)
for i in s[y:n+1:1]:
    if i=="1":
        for w in range(1,K+1):
            a=y+w
            aa=y-w
            if s[a:a+1:]=="1":
                x+=0
            elif s[a:a+1:]=="0":
                x+=1 

            if y>1:
                if s[aa:aa-1:-1]=="1":
                    x=x+0
                elif s[aa:aa-1:-1]=="0":
                    x=x+1


        x+=1
    y+=1
print(x) 

 