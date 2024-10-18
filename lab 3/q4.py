import pandas as pd
import numpy as np

# Load the data from the Excel file
data = pd.read_excel('Lab3.2.xlsx', sheet_name='Sheet1')

# Get the measured count rates for Sample 5 (as the diluted source)
measured_counts_sample_5 = data.iloc[4, 1:]

# Using the tau from the non-paralyzable model fits (slopes) to calculate correction factors
tau_values = {1: 9.32e-5, 2: 4.35e-4, 3: 9.23e-4, 4: 1.53e-3}

# Calculate the correction factors
correction_factors = {}
for i, shelf in enumerate(measured_counts_sample_5.index):
    tau = tau_values[i+1]
    correction_factor = measured_counts_sample_5[shelf] / (1 - (measured_counts_sample_5[shelf] * tau))
    correction_factors[shelf] = correction_factor

print(f"Dead time correction factors:", correction_factors)