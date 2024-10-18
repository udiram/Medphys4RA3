import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the Excel file
data = pd.read_excel('Lab3.2.xlsx', sheet_name='Sheet1')

# Assuming Sample 5's measured count rate as the true count rate for Sample 5 (approximation).
sample_5 = data.iloc[4, 1:]  # Sample 5's measured counts (S1 to S4)

# Calculate the true count rate for each sample using this assumption
true_count_rate = data.iloc[:, 1:].div(sample_5, axis=1).multiply(sample_5.mean())

# Plot measured count rate vs true count rate
plt.figure(figsize=(8,6))
for i in range(len(data)):
    plt.plot(data.iloc[i, 1:], true_count_rate.iloc[i, :], 'o-', label=f'Sample {i+1}')

plt.plot([0, data.max().max()], [0, data.max().max()], '--', label='Line of Equality', color='black')
plt.xlabel('Measured Count Rate (Counts per second)')
plt.ylabel('True Count Rate (Counts per second)')
plt.title('Measured Count Rate vs True Count Rate')
plt.legend()
plt.grid(True)
plt.show()