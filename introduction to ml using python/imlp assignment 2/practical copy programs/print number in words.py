x=input("enter a number to print its word form: ")
s=list(x)
n=""
for i in range(0,len(s)):
    if s[i]=="1":
        n+="One "
    elif s[i]=="2":
        n+="Two "
    elif s[i]=="3":
        n+="Three "
    elif s[i]=="4":
        n+="Four "
    elif s[i]=="5":
        n+="Five "
    elif s[i]=="6":
        n+="Six "
    elif s[i]=="7":
        n+="Seven "
    elif s[i]=="8":
        n+="Eight "
    elif s[i]=="9":
        n+="Nine "
    else:
        n+="Zero "
    #print(" ")    
print(n)