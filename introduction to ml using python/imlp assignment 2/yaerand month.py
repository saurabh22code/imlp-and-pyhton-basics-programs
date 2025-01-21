import calendar  
  
year = int(input ("Please enter the Year: ")) # Here, it will take the year  
month = int(input ("Please enter the month: "))    # Here, it will take the month  
  
# Now, we will display the calendar  
print("The Calendar of: ", calendar.month(year, month))  