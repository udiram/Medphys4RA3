# Re-importing necessary libraries and running the code from the start.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the actual data from the uploaded CSV file
data = pd.read_csv('Lab32.csv')

# x represents the relative activity, for which we'll assume x = 5 for Sample 5.
relative_activity = pd.Series([1, 2, 3, 4, 5])

# Calculate 1/C_m (1 over measured count rate) and 1/x (1 over relative activity)
inv_measured_rate = data.iloc[:, 1:].apply(lambda x: 1 / x)
inv_relative_activity = 1 / relative_activity

# Plotting 1/C_m as a function of 1/x and performing a linear fit to determine the dead time
fig, ax = plt.subplots(figsize=(8, 6))

fits = {}
for i, col in enumerate(inv_measured_rate.columns):
    # Plot data points
    ax.plot(inv_relative_activity, inv_measured_rate[col], 'o-', label=f'Sample {i + 1}')

    # Fit a line for each sample
    coeffs = np.polyfit(inv_relative_activity, inv_measured_rate[col], 1)
    fits[col] = coeffs  # Store fit coefficients (slope and intercept)

    # Plot the fitted line
    ax.plot(inv_relative_activity, np.polyval(coeffs, inv_relative_activity), '--')

# Set labels and title
ax.set_xlabel('1 / Relative Activity (1/x)')
ax.set_ylabel('1 / Measured Count Rate (1/C_m)')
ax.set_title('1 / Measured Count Rate vs 1 / Relative Activity (Non-Paralyzable Model)')
ax.legend()
ax.grid(True)

# Display the plot
plt.savefig('q2.png')
plt.show()

# Extracting dead time (y-intercept) from the fit results
dead_time_values = {f'Sample {i + 1}': coeffs[1] for i, coeffs in enumerate(fits.values())}

print(dead_time_values)
