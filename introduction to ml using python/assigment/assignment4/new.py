import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5]
temperature = [22, 24, 20, 23, 25]

# Create the plot
plt.plot(days, temperature, marker='o', linestyle='-', color='b')

# Add title and labels
plt.title('Temperature Over Five Days')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')

# Show the plot
plt.grid(True)
plt.show()
