"""
Q.10.Create a pythn programme to read a csv file and find the sum of a specific column

Here’s a Python program that reads a CSV file and calculates the sum of a specific column:"""
import csv

# Function to calculate the sum of a specific column in a CSV file
def sum_column_in_csv(file_name, column_name):
    try:
        # Open the CSV file in read mode
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)  # Use DictReader to access columns by name
            
            total = 0
            count = 0
            
            # Iterate through each row in the CSV file
            for row in reader:
                # Check if the column exists and if the value is numeric
                if column_name in row and row[column_name].replace('.', '', 1).isdigit():
                    total += float(row[column_name])  # Convert to float and add to total
                    count += 1

            if count == 0:
                print(f"No valid data found in the column '{column_name}'.")
                return
            
            # Print the sum of the column
            print(f"The sum of the column '{column_name}' is: {total:.2f}")
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_name = "data.csv"  # Replace with your CSV file path
column_name = "Amount"  # Replace with the column name you want to sum

sum_column_in_csv(file_name, column_name)
