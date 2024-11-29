import numpy as np
import matplotlib.pyplot as plt
# Prepare data for plotting with uncertainties
observed_rates = []
true_rates = []
observed_uncertainties = []
true_uncertainties = []

# Given data
sample_counts = {
    "Sample 1": {"Shelf 1": 33891, "Shelf 2": 16946, "Shelf 3": 9431, "Shelf 4": 6002},
    "Sample 2": {"Shelf 1": 41940, "Shelf 2": 27330, "Shelf 3": 16700, "Shelf 4": 11202},
    "Sample 3": {"Shelf 1": 43895, "Shelf 2": 33848, "Shelf 3": 22331, "Shelf 4": 15344},
    "Sample 4": {"Shelf 1": 44630, "Shelf 2": 38470, "Shelf 3": 27343, "Shelf 4": 19414},
    "Sample 5": {"Shelf 1": 45029, "Shelf 2": 41086, "Shelf 3": 31847, "Shelf 4": 22452},
}

# Constants
tau = 200e-6  # Dead time in seconds

# Process each sample and shelf
for sample, shelves in sample_counts.items():
    for shelf, count in shelves.items():
        # Calculate measured rate and uncertainty
        measured_rate = count / 10.0  # counts per second
        measured_uncertainty = np.sqrt(count) / 10.0  # uncertainty in counts per second

        # Apply dead time correction
        corrected_rate = measured_rate / (1 - (measured_rate * tau))

        # Propagate uncertainty for the true rate
        corrected_uncertainty = measured_uncertainty / (1 - (measured_rate * tau)) ** 2

        # Append rates and uncertainties to lists
        observed_rates.append(measured_rate)
        true_rates.append(corrected_rate)
        observed_uncertainties.append(measured_uncertainty)
        true_uncertainties.append(corrected_uncertainty)

# Adjusting the scaling for better visibility
plt.figure(figsize=(8, 6))

# Create the scatter plot with error bars
plt.errorbar(true_rates, observed_rates, xerr=true_uncertainties, yerr=observed_uncertainties,
             fmt='o', color='blue', label="Measured vs. True Count Rates", ecolor='gray', capsize=3)

# Plot the ideal y=x line for comparison
plt.plot([min(true_rates), max(true_rates)], [min(true_rates), max(true_rates)],
         color='red', linestyle='--', label="Line of Equality")

# Set the axis labels and title
plt.xlabel("True Count Rate (counts/s)")
plt.ylabel("Measured Count Rate (counts/s)")
plt.title("Measured vs. True Count Rates with Uncertainties")

# Adjust the limits for better visual coherence
plt.xlim(0, max(true_rates) * 1.1)
plt.ylim(0, max(observed_rates) * 1.1)

# Add a legend and grid
plt.legend()
plt.grid(True)

plt.savefig('q1.png')
# Show the plot
plt.show()
