#conversion rate (as of the latest known rate; this can change )
conversion_rate= float(input("Enter the conversion rate:"))
#Example rate : 1 USD =87.38 INR

#get the amount is U.S dollars from the user
usd_amount=float(input("Enter the USD amount:"))

#convert to indian rupees
inr_amount=usd_amount*conversion_rate

#display the result
print(f"{usd_amount} U.S. Dollars is equivalent to {inr_amount} indian rupees")