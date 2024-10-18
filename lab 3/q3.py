import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the Excel file
data = pd.read_csv('Lab32.csv')

# x represents the relative activity, for which we'll assume x = 5 for Sample 5 as indicated in the instructions.
relative_activity = pd.Series([1, 2, 3, 4, 5])

# Calculate ln(C_m/x) for each shelf
log_measured_rate = data.iloc[:, 1:].div(relative_activity.values, axis=0).apply(np.log)

# Plot ln(C_m/x) as a function of x and perform linear fitting to estimate the dead time for paralyzable model
fig, ax = plt.subplots(figsize=(8, 6))

for i, col in enumerate(log_measured_rate.columns):
    ax.plot(relative_activity, log_measured_rate[col], 'o-', label=f'Sample {i+1}')

# Fit a line to each sample
fits_log = {}
for col in log_measured_rate.columns:
    coeffs = np.polyfit(relative_activity, log_measured_rate[col], 1)
    fits_log[col] = coeffs
    ax.plot(relative_activity, np.polyval(coeffs, relative_activity), '--')

ax.set_xlabel('Relative Activity (x)')
ax.set_ylabel('ln(C_m / x)')
ax.set_title('ln(C_m / x) vs Relative Activity (Paralyzable Model)')
ax.legend()
ax.grid(True)

plt.show()

print(f"Dead Time values (τ) for paralyzable model:", fits_log)