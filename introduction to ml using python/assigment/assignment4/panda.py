import pandas as pd

# Data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [23, 25, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create DataFrame
df = pd.DataFrame(data)
print("DataFrame:\n", df)


# Display the first two rows
print("First two rows:\n", df.head(2))



# Add new column "Score"
df['Score'] = [85, 90, 78, 92]
print("DataFrame with 'Score' column:\n", df)
