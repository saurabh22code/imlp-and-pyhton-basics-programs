import matplotlib.pyplot as plt

# Data
labels = ['Coffee', 'Tea', 'Juice', 'Water']
sizes = [45, 30, 15, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
explode = (0.1, 0, 0, 0)  # explode the 1st slice (Coffee)

# Create the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')
plt.show()