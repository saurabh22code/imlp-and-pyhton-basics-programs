#WAP  in python to create a regular expression to retrieve words  having 5 characters
import re
str="one two @ $ ^ & * three four five six seven 8 9 10"
result=re.findall(r"\W",str)
print(result)


#WAP in to find the words which are stating with a
str1="an apple a day keeps the doctore away"
result1=re.findall(r'\ba[\w]*',str1)
print(result1)

#WAP to create a regular exp. to replace a string with a new string
str2="kumbh mela will be conducted in Aligarh and Agra in India"
result2=re.sub(r"A[\w]*","prayagraj",str2)
print(result2)