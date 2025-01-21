#WAP tp retrieve all the words starting with digits 
import re
str="the meeting will be conducted on 1st and 2nd of every month"
x=re.findall(r'\d',str)
print()