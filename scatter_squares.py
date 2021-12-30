import matplotlib.pyplot as plt
from fontTools.merge import cmap

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)
# ax.scatter(x_values, y_values, s=10, c=(0.8862745, 0, 0.4549))
# ax.scatter(x_values, y_values, s=10, c=(226/255, 0, 116/255))
# ax.plot(x_values, y_values, linewidth=1)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", which='major', labelsize=14, color='red')

# set the range for each axis.
ax.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
