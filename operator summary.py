import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Define the data
data = {
    "20% horizontal": [1.0943, 3.6262, 1.0122],
    "20% lateral": [0.7369, 4.1309, 1.5590],
    "30% horizontal": [2.1928, 4.6543, 2.6465],
    "30% lateral": [0.1653, 1.5639, 0.2554],
    "40% horizontal": [1.4725, 7.0495, 1.3459],
    "40% lateral": [0.0029, 8.0539, 0.0004]
}

# Define the weights
weights = [0.3, 0.4, 0.3]

# Define the x labels
x_labels = ["20% horizontal", "20% lateral", "30% horizontal", "30% lateral", "40% horizontal", "40% lateral"]

# Calculate the weighted values
weighted_values = []
for label in x_labels:
    values = data[label]
    weighted_value = sum(w * v for w, v in zip(weights, values))
    weighted_values.append(weighted_value)

# Find the index of the smallest value
min_index = np.argmin(weighted_values)

# Create a bar chart with a similar style
fig, ax = plt.subplots(figsize=(8, 6))

# Set x positions for the bars
x_pos = np.arange(len(x_labels))

# Set a narrower bar width
bar_width = 0.25

# Create the bar chart with the same color scheme
colors = ['red' if i == min_index else 'royalblue' for i in range(len(x_labels))]
bars = plt.bar(x_pos, weighted_values, bar_width, align='center', alpha=0.75, color=colors)

# Set x tick labels and rotation
plt.xticks(x_pos, x_labels, rotation=20)

# Label the axes
plt.xlabel('Cases')
plt.ylabel('Weighted Value')

# Add data labels on top of the bars
for bar, value in zip(bars, weighted_values):
    plt.text(bar.get_x() + bar.get_width() / 2, value, f'{value:.2f}', ha='center', va='bottom')
blue_patch = Patch(color='royalblue', label='Total value')
red_patch = Patch(color='red', label='Minimum value')
bar_legend = ax.legend(handles=[blue_patch, red_patch], loc='upper left', fontsize=10)
ax.add_artist(bar_legend)
# Show the plot
plt.tight_layout()
plt.savefig("sum_acc_operator.png", bbox_inches='tight')
plt.show()
