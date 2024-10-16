import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Extracting the data for voltage and cps (count rate)
voltage = np.array([360, 380, 410, 430, 460, 500, 520, 550, 570, 590])
count_rate = np.array([0, 0, 1.41, 9.32, 9.34, 9.87, 9.34, 9.20, 9.30, 10.21])

# Identifying the plateau region (typically where the count rate stays relatively constant)
# For this data, the plateau seems to be between 430V and 570V
plateau_voltage = voltage[3:8]  # Voltage between 430V and 570V
plateau_cps = count_rate[3:8]

# Linear fit to the plateau region
slope, intercept, r_value, p_value, std_err = linregress(plateau_voltage, plateau_cps)

# Generating the fitted line
fitted_line = slope * plateau_voltage + intercept
# Plotting the data as a discrete set of points without connecting lines between them
# Define the error for both x (voltage) and y (count rate)
voltage_error = 10  # As mentioned in the image, the voltage error is ±10V
count_rate_error = 0.1 * count_rate  # Assuming 10% error in count rate measurement

# Plotting with error bars
plt.figure(figsize=(8, 6))
plt.errorbar(voltage, count_rate, yerr=count_rate_error, xerr=voltage_error, fmt='bo', label='Count Rate Data', markersize=8, capsize=5)
plt.plot(plateau_voltage, fitted_line, 'r--', label=f'Plateau Fit: slope = {slope:.4f}')
plt.axvline(x=460, color='green', linestyle='--', label='Chosen Operating Voltage = 460V')
plt.xlabel('Applied Voltage (V)')
plt.ylabel('Count Rate (cps)')
plt.title('Count Rate vs Applied Voltage for GM Detector (Discrete with Error Bars)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()


# Comment on the slope of the plateau region
slope, intercept, std_err
