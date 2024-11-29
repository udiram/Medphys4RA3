import matplotlib.pyplot as plt
from scipy.stats import linregress

# Data from the user's document
channel_numbers = [213.30, 79.25, 321.41, 351.52, 354.65, 567.34]
peak_energies = [662, 193, 1173, 1332, 1368, 2754]

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(channel_numbers, peak_energies)

# Generate points for the regression line
channel_range = range(int(min(channel_numbers)) - 10, int(max(channel_numbers)) + 10)
calibration_line = [slope * x + intercept for x in channel_range]

# Plotting the calibration plot
plt.figure(figsize=(8, 6))
plt.scatter(channel_numbers, peak_energies, color='blue', label='Calibration Points')
plt.plot(channel_range, calibration_line, color='red', linestyle='--', label=f'Fit: Energy = {slope:.2f} * Channel {intercept:.2f}')
plt.xlabel('Channel Number')
plt.ylabel('Peak Energy (keV)')
plt.title('Calibration Plot: Peak Energy vs. Channel Number')
plt.legend()
plt.grid(True)
plt.savefig('calibration_plot.png')
plt.show()

# Display the calibration equation
print(slope, intercept, r_value**2)