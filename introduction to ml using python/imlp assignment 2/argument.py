#pogram to demonstrate *args and **kwargs
def sum(a,b,c):
    s=a+b+c
    print(f"Sum of {a},{b},{c} is {s}")
sum(12,21,22)
#the above function is resticted to take only three input but with *args we can make it universal as the following program 

def SumAll(*num):
    sum=0
    for i in num:
        sum+=i
    print(f"the sum of given numbers is {sum}")
SumAll(12,12,334,5,667,7,8,999,754)



#for keyword arguments:ṇ
def spreaddata(**data):
    for key, value in data.items():
        print("{} is {}".format(key,value))
spreaddata(name="SAURABH KUMAR", age=20, address="patratu")   