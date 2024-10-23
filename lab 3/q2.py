import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the actual data from the uploaded CSV file
data = pd.read_csv('Lab32.csv')

# Assume x = 5 for Sample 5 as relative activity
relative_activity = pd.Series([1, 2, 3, 4, 5])

# Calculate 1/C_m (1 over measured count rate) and 1/x (1 over relative activity)
inv_measured_rate = data.iloc[:, 1:].apply(lambda x: 1 / x)
inv_relative_activity = 1 / relative_activity

# Perform a linear fit to determine the dead time (intercept)
fits = {}
for i, col in enumerate(inv_measured_rate.columns):
    # Fit a line for each sample
    coeffs = np.polyfit(inv_relative_activity, inv_measured_rate[col], 1)
    fits[col] = coeffs  # Store fit coefficients (slope and intercept)

# Extracting dead time (y-intercept) and slope from the fit results
dead_time_values = {f'Shelf {i + 1}': {"R2": np.corrcoef(inv_relative_activity, inv_measured_rate[col])[0, 1]**2,
                                        "tau (µs)": round(coeffs[1] * 1e6, 2)} for i, coeffs in enumerate(fits.values())}

# Creating the summary table as a pandas dataframe
dead_time_df = pd.DataFrame.from_dict(dead_time_values, orient='index').reset_index()
dead_time_df.columns = ['Shelf #', 'R2', 'τ (µs)']

# Display the summary table
print(dead_time_df)


# Plotting 1/C_m as a function of 1/x and performing a linear fit to determine the dead time
fig, ax = plt.subplots(figsize=(8, 6))

for i, col in enumerate(inv_measured_rate.columns):
    # Plot data points
    ax.plot(inv_relative_activity, inv_measured_rate[col], 'o-', label=f'Shelf {i + 1}')

    # Fit a line for each sample
    coeffs = np.polyfit(inv_relative_activity, inv_measured_rate[col], 1)

    # Plot the fitted line
    ax.plot(inv_relative_activity, np.polyval(coeffs, inv_relative_activity), '--')

# Set labels and title
ax.set_xlabel('1 / Relative Activity (1/x)')
ax.set_ylabel('1 / Measured Count Rate (1/C_m)')
ax.set_title('1 / Measured Count Rate vs 1 / Relative Activity (Non-Paralyzable Model)')
ax.legend()
ax.grid(True)

# Save the plot
plt.savefig('q2.png')

# Display the plot
plt.show()
