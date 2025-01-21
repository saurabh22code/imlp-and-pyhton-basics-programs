import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the two datasets
dataset_a = [10, 25, 35, 45, 60]  # Min = 10, Q1 = 25, Median = 35, Q3 = 45, Max = 60
dataset_b = [5, 20, 30, 50, 80]   # Min = 5, Q1 = 20, Median = 30, Q3 = 50, Max = 80

# Calculate the central tendency (Median) and spread (IQR, Range) for each dataset
def calculate_stats(data):
    min_val = np.min(data)
    q1 = np.percentile(data, 25)
    median = np.median(data)
    q3 = np.percentile(data, 75)
    max_val = np.max(data)
    
    # Range and IQR
    range_val = max_val - min_val
    iqr = q3 - q1
    
    return min_val, q1, median, q3, max_val, range_val, iqr

# Get stats for both datasets
stats_a = calculate_stats(dataset_a)
stats_b = calculate_stats(dataset_b)

# Print the stats
print("Dataset A:")
print(f"Min: {stats_a[0]}, Q1: {stats_a[1]}, Median: {stats_a[2]}, Q3: {stats_a[3]}, Max: {stats_a[4]}")
print(f"Range: {stats_a[5]}, IQR: {stats_a[6]}\n")

print("Dataset B:")
print(f"Min: {stats_b[0]}, Q1: {stats_b[1]}, Median: {stats_b[2]}, Q3: {stats_b[3]}, Max: {stats_b[4]}")
print(f"Range: {stats_b[5]}, IQR: {stats_b[6]}\n")

# Visualize the datasets with boxplots
plt.figure(figsize=(10, 6))
sns.boxplot(data=[dataset_a, dataset_b], showfliers=True)
plt.xticks([0, 1], ['Dataset A', 'Dataset B'])
plt.title("Boxplot Comparison: Dataset A vs. Dataset B")
plt.show()
