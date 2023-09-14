import matplotlib.pyplot as plt
import numpy as np

# Data
accumulation_on_right = [2.6465, 0.2554]
accumulation_on_left = [2.1928, 0.1653]
accumulation_on_center = [4.6543, 1.5639]
operators = ['left', 'center', 'right']

# Create a figure and axis
fig, ax = plt.subplots()

# Calculate bar positions
bar_positions = np.arange(len(operators))

# Plot bars for accumulation_on_right
bars1 = ax.bar(bar_positions - 0.2, [accumulation_on_left[0], accumulation_on_center[0], accumulation_on_right[0]],
               width=0.4, color='red', label='horizontal', alpha=0.65)

# Plot bars for accumulation_on_center
bars2 = ax.bar(bar_positions + 0.2, [accumulation_on_left[1], accumulation_on_center[1], accumulation_on_right[1]],
               width=0.4, color='blue', label='lateral', alpha=0.65)

# Set labels and title
ax.set_xlabel('Operators')
ax.set_ylabel('Accumulation on each operator (m$^2 \cdot \mathrm{s})$')

ax.set_xticks(bar_positions)
ax.set_xticklabels(operators)
ax.legend()

# Adjust the x-axis limits to align the bars
ax.set_xlim(-0.5, len(operators) - 0.5)

# Add data labels on top of bars
def add_data_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.4f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_data_labels(bars1)
add_data_labels(bars2)

# Show the plot
plt.savefig('operator_accumulation_trend_30.png')
plt.savefig('operator_accumulation_trend_30.svg', format="svg")
plt.tight_layout()
plt.show()
