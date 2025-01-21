#write a program to convert U.S. dollars to Indian rupees.

U_S_dollar=float(input("enter the current rate of 1 U.S.Dollar :"))
#taking input of the U.S. to convert it to indian rupee
Dollar=int(input("Enter the amount in U.S. dollar: "))

#multiplying the U.S. dollar to current rate of 1$ in
indian_rupees=Dollar*U_S_dollar
print(Dollar,"$ =",indian_rupees,"Indian Rupees")
