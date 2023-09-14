import matplotlib.pyplot as plt
import numpy as np

# Data
accumulation_on_right = [1.2479, 1.6650]
accumulation_on_left = [1.2962, 1.1959]
accumulation_on_center = [3.2527, 2.2186]
operators = ['left', 'center', 'right']

# Create a figure and axis
fig, ax = plt.subplots()

# Calculate bar positions
bar_positions = np.arange(len(operators))

# Plot bars for accumulation_on_right
ax.bar(bar_positions - 0.2, [accumulation_on_left[0], accumulation_on_center[0], accumulation_on_right[0]],
       width=0.4, color='red', label='horizontal',alpha=0.65)

# Plot bars for accumulation_on_center
ax.bar(bar_positions + 0.2, [accumulation_on_left[1], accumulation_on_center[1], accumulation_on_right[1]],
       width=0.4, color='blue', label='lateral', alpha=0.65)

# Set labels and title
ax.set_xlabel('Operators')
ax.set_ylabel('Accumulation on each operator')

ax.set_xticks(bar_positions)
ax.set_xticklabels(operators)
ax.legend()

# Adjust the x-axis limits to align the bars
ax.set_xlim(-0.5, len(operators) - 0.5)

# Show the plot
plt.savefig('operator_accumulation_trend_20.png')
plt.tight_layout()
plt.show()

