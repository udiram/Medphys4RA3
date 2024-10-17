import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

import pandas as pd

# Data from the images
data = {
    "Sample": ["Sample 1"] * 4 + ["Sample 2"] * 4 + ["Sample 3"] * 4 + ["Sample 4"] * 4 + ["Sample 5"] * 4 + ["Calibration"] * 4,
    "Shelf": ["Shelf 1", "Shelf 2", "Shelf 3", "Shelf 4"] * 6,
    "Time (s)": [10] * 24,
    "Counts": [
        33891, 16996, 9431, 6002,  # Sample 1
        41940, 27330, 16780, 11202, # Sample 2
        43895, 33848, 22331, 15344, # Sample 3
        44630, 38470, 27393, 19414, # Sample 4
        45029, 41086, 31047, 22452, # Sample 5
        1938, 664, 341, 216          # Calibration
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate measured count rate (Ċm)
df['C_dot_m'] = df['Counts'] / df['Time (s)']

# Create a list to store results for each sample's linear fit
fit_results = []

# Plot ln(Ċm / x) vs. x for each sample and perform linear regression
plt.figure(figsize=(14, 10))
samples = df['Sample'].unique()

for sample in samples:
    sample_data = df[df['Sample'] == sample]
    x = np.arange(1, 5)  # Shelf numbers 1 to 4
    ln_C_dot_m_over_x = np.log(sample_data['C_dot_m'] / x)

    # Linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, ln_C_dot_m_over_x)
    fit_results.append({"Sample": sample, "Slope": slope, "Intercept": intercept, "R-squared": r_value**2})

    # Plot the data and the fit
    plt.plot(x, ln_C_dot_m_over_x, 'o', label=f'{sample} data')
    plt.plot(x, slope * x + intercept, '-', label=f'{sample} fit: slope={slope:.4f}')

# Plot formatting
plt.title('ln(Ċm / x) vs. x for Each Sample')
plt.xlabel('Shelf Number (x)')
plt.ylabel('ln(Ċm / x)')
plt.legend()
plt.grid()
plt.savefig('ln_Cm_over_x_vs_x.png')
plt.show()

# Display the fit results
fit_results_df = pd.DataFrame(fit_results)
fit_results_df['Dead Time (τ) [s]'] = -1 / fit_results_df['Slope']

# Drop the intercept and slope columns as requested
fit_results_df = fit_results_df.drop(columns=['Intercept', 'Slope'])
print(fit_results_df)