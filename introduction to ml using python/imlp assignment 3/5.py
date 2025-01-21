'''
Q.5. Create a python file that reads a csv file named data.csv and calculate the average value of a specific column

Here is a Python program that reads a CSV file named data.csv, calculates the average value of a specific column, and prints the result:
'''    
import csv

# Function to calculate the average value of a specific column
def calculate_column_average(file_name, column_name):
    try:
        # Open the CSV file in read mode
        with open(file_name, "r") as csvfile:
            reader = csv.DictReader(csvfile)  # Use DictReader to access columns by name
            total = 0
            count = 0
            
            for row in reader:
                # Ensure the column exists and add its value
                if column_name in row and row[column_name].strip().isdigit():
                    total += float(row[column_name])  # Convert the value to float
                    count += 1
            
            # Check if there were valid rows
            if count == 0:
                print(f"No valid data found in the column '{column_name}'.")
                return
            
            # Calculate the average
            average = total / count
            print(f"The average value of the column '{column_name}' is: {average:.2f}")
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except KeyError:
        print(f"The column '{column_name}' does not exist in the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# Replace 'data.csv' with the actual file name and 'ColumnName' with the column to calculate
file_name = "data.csv"
column_name = "ColumnName"  # Replace with the column name to calculate
calculate_column_average(file_name, column_name)
