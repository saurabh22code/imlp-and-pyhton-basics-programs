import os
print(os.getcwd())
print(os.listdir())
#os.mkdir("test")
print(os.listdir())
#os.rmdir("test")
#print(os.listdir())


import random
print(random.randint(1,10))
print(random.random())
print(random.randbytes(10))



import calendar
print(calendar.month(2024,12))
#print(calendar.calendar.isleap(2024))
print(calendar.datetime)
print(calendar.calendar(2024))



import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour) 
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().microsecond)


import sys
print(sys.version)
print(sys.version_info)
print(sys.path)
print(sys.platform)
