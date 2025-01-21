import matplotlib.pyplot as plt

# Data
labels = ['Coffee', 'Tea', 'Juice', 'Water']
sizes = [45, 30, 15, 10]

# Create the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ffcc00', '#66b3ff', '#ff6666', '#99ff99'])

# Set the title of the chart
plt.title('Beverage Preferences Survey')

# Display the pie chart
plt.show()