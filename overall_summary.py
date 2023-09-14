import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Define the data
data = {
    "20% horizontal": [0.0031, 2.08, 1891.2],
    "20% lateral": [0.0034, 2.34, 3963.35],
    "30% horizontal": [0.0058, 3.31, 1861.17],
    "30% lateral": [0.0059, 0.75, 5280.52],
    "40% horizontal": [0.0038, 3.67, 1652.71],
    "40% lateral": [0.0072, 3.22, 4670.90]
}

# Define the weights
weights = [0.3, 0.4, 0.3]

# Calculate the maximum values for each column
column_max = [max(values[i] for values in data.values()) for i in range(3)]

# Normalize the data and calculate the weighted values
normalized_values = {}
weighted_values = {}
for case, values in data.items():
    normalized_values[case] = [value / column_max[i] for i, value in enumerate(values)]
    weighted_values[case] = sum(w * v for w, v in zip(weights, normalized_values[case]))

# Find the index of the smallest weighted value
min_index = np.argmin(list(weighted_values.values()))

# Create a bar chart with a similar style
fig, ax = plt.subplots(figsize=(8, 6))

# Set x positions for the bars
x_pos = np.arange(len(data))

# Set a narrower bar width
bar_width = 0.25

# Create the bar chart with the same color scheme
colors = ['red' if i == min_index else 'royalblue' for i in range(len(data))]
bars = plt.bar(x_pos, list(weighted_values.values()), bar_width, align='center', alpha=0.75, color=colors)

# Set x tick labels and rotation
plt.xticks(x_pos, data.keys(), rotation=20)

# Label the axes
plt.xlabel('Cases')
plt.ylabel('Weighted Value')

# Add data labels on top of the bars
for bar, value in zip(bars, weighted_values.values()):
    plt.text(bar.get_x() + bar.get_width() / 2, value, f'{value:.2f}', ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()
