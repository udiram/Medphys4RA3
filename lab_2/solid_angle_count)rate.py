import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import linregress

shelf_data = {
    "Shelf": [5, 4, 3, 2],
    "Counts": [289, 494, 913, 2846],
    "cps": [2.89, 4.94, 9.13, 24.46],
    "Distance (cm)": [5.7, 4.3, 3.1, 1.7]
}

# Convert data into a DataFrame
df_shelf = pd.DataFrame(shelf_data)

# Calculate the solid angle (Ω) for each distance using the given formula
a = 0.5  # radius of the detector in cm

df_shelf['Solid Angle (Ω)'] = np.pi * (a**2) / (df_shelf['Distance (cm)']**2)

# Perform linear regression to get the line of best fit for the experimental data
slope, intercept, r_value, p_value, std_err = linregress(df_shelf['Solid Angle (Ω)'], df_shelf['cps'])
line_of_best_fit = slope * df_shelf['Solid Angle (Ω)'] + intercept
# It seems that there might be a KeyError because the column is not properly created. Let's recalculate it.
# Calculate the solid angle using the standard form model (New Solid Angle)
df_shelf['New Solid Angle (Ω)'] = 2 * np.pi * (1 - df_shelf['Distance (cm)'] / np.sqrt(a**2 + df_shelf['Distance (cm)']**2))

# Now plotting again with the correct data
plt.figure(figsize=(8, 6))

# Experimental data plot (based on counts)
plt.plot(df_shelf['Solid Angle (Ω)'], df_shelf['cps'], 'bo', label='Experimental Data', markersize=8)

# Approximation model plot (πa^2/d^2)
plt.plot(df_shelf['Solid Angle (Ω)'], df_shelf['cps'], 'r--', label='Approximation: πa^2/d^2')

# Standard form model plot (new solid angle formula)
plt.plot(df_shelf['New Solid Angle (Ω)'], df_shelf['cps'], 'g-.', label='Standard Form: 2π(1 - d/sqrt(a^2 + d^2))')

# Line of best fit for experimental data
plt.plot(df_shelf['Solid Angle (Ω)'], line_of_best_fit, 'm-', label=f'Best Fit: R² = {r_value**2:.4f}')

plt.xlabel('Solid Angle (Ω)')
plt.ylabel('Count Rate (cps)')
plt.title('Comparison of Experimental Data, Approximation, and Standard Form')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()


