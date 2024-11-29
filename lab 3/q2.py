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

# Assume uncertainty in measured count rates as sqrt of the count rate (Poisson statistics)
measured_rate_uncertainty = data.iloc[:, 1:].apply(lambda x: np.sqrt(x))

# Calculate the uncertainty in 1/C_m using error propagation
inv_measured_rate_uncertainty = measured_rate_uncertainty / data.iloc[:, 1:]**2

# Perform a linear fit to determine the dead time (intercept) and incorporate errors in y
fits = {}
for i, col in enumerate(inv_measured_rate.columns):
    # Fit a line using a weighted least squares fit, with weights as the inverse of the squared uncertainties
    weights = 1 / inv_measured_rate_uncertainty[col]**2
    coeffs = np.polyfit(inv_relative_activity, inv_measured_rate[col], 1, w=weights)
    fits[col] = coeffs  # Store fit coefficients (slope and intercept)

# Extracting dead time (y-intercept) and slope from the fit results
dead_time_values = {f'Shelf {i + 1}': {"R2": np.corrcoef(inv_relative_activity, inv_measured_rate[col])[0, 1]**2,
                                        "tau (µs)": round(coeffs[1] * 1e6, 2)} for i, coeffs in enumerate(fits.values())}

# Creating the summary table as a pandas dataframe
dead_time_df = pd.DataFrame.from_dict(dead_time_values, orient='index').reset_index()
dead_time_df.columns = ['Shelf #', 'R2', 'τ (µs)']

# Display the summary table
print(dead_time_df)

# Plotting 1/C_m as a function of 1/x and performing a linear fit with error bars
fig, ax = plt.subplots(figsize=(8, 6))

for i, col in enumerate(inv_measured_rate.columns):
    # Plot data points with error bars
    ax.errorbar(inv_relative_activity, inv_measured_rate[col],
                yerr=inv_measured_rate_uncertainty[col], fmt='o-', label=f'Shelf {i + 1}')

    # Fit a line for each sample
    coeffs = fits[col]

    # Plot the fitted line
    ax.plot(inv_relative_activity, np.polyval(coeffs, inv_relative_activity), '--')

# Set labels and title
ax.set_xlabel('1 / Relative Activity (1/x)')
ax.set_ylabel('1 / Measured Count Rate (1/C_m)')
ax.set_title('1 / Measured Count Rate vs 1 / Relative Activity (Non-Paralyzable Model) with Error Bars')
ax.legend()
ax.grid(True)

# Save the plot
plt.savefig('q2_with_errors.png')

# Display the plot
plt.show()
