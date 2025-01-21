# program to check a year is leap year or not
#taking input of year
year=int(input("Enter year: "))

#checking whether the year is leap year or not
if year%4==0 and year%100==0 and year%400==0:
    #printing leap year if it is!
    print(f"{year} is a leap year")
else:
    #printing not leap year if it is not!
    print(f"{year} is not a leap year")