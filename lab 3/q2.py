import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the Excel file
data = pd.read_excel('Lab3.2.xlsx', sheet_name='Sheet1')

# x represents the relative activity, for which we'll assume x = 5 for Sample 5 as indicated in the instructions.
relative_activity = pd.Series([1, 2, 3, 4, 5])

# Calculate 1/C_m (1 over measured count rate) and 1/x (1 over relative activity)
inv_measured_rate = data.iloc[:, 1:].apply(lambda x: 1/x)
inv_relative_activity = 1 / relative_activity

# Plotting 1/C_m as a function of 1/x and performing a linear fit to determine the dead time using non-paralyzable model
fig, ax = plt.subplots(figsize=(8, 6))

for i, col in enumerate(inv_measured_rate.columns):
    ax.plot(inv_relative_activity, inv_measured_rate[col], 'o-', label=f'Sample {i+1}')

# Fit a line for each sample to estimate the dead time (τ)
fits = {}
for col in inv_measured_rate.columns:
    coeffs = np.polyfit(inv_relative_activity, inv_measured_rate[col], 1)
    fits[col] = coeffs
    ax.plot(inv_relative_activity, np.polyval(coeffs, inv_relative_activity), '--')

ax.set_xlabel('1 / Relative Activity (1/x)')
ax.set_ylabel('1 / Measured Count Rate (1/C_m)')
ax.set_title('1 / Measured Count Rate vs 1 / Relative Activity (Non-Paralyzable Model)')
ax.legend()
ax.grid(True)

plt.show()

print(f"Dead Time values (τ):", fits)