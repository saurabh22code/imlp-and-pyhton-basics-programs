def upto_n(n):
    if n==0:
        print("the anser is 0")
    else:
        return int(n)+upto_n(n-1)
    

upto_n(int(10))