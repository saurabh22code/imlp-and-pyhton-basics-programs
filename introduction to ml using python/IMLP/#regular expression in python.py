#regular expression in python
import re
str=" cat mat bat man"
x=re.search(r'm\w\w',str)
print(x.group())
