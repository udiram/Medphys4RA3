import matplotlib.pyplot as plt
import numpy as np

# Given data for Sample 6 measured counts (considered as true counts approximation for other samples)
# Example measured counts for Sample 6 (counts/10s) from the document
sample_6_counts = {
    "Shelf 1": 45029,
    "Shelf 2": 41086,
    "Shelf 3": 31847,
    "Shelf 4": 22452,
}

# Dead time of GM counter (assuming tau = 200 microseconds = 0.0002 s)
tau = 0.0002

# Conversion of counts to count rate (per second)
sample_6_rate = {shelf: count / 10.0 for shelf, count in sample_6_counts.items()}

# Data for other samples (counts/10s) from the document
sample_counts = {
    "Sample 1": {"Shelf 1": 33891, "Shelf 2": 16946, "Shelf 3": 9431, "Shelf 4": 6002},
    "Sample 2": {"Shelf 1": 41940, "Shelf 2": 27330, "Shelf 3": 16700, "Shelf 4": 11202},
    "Sample 3": {"Shelf 1": 43895, "Shelf 2": 33848, "Shelf 3": 22331, "Shelf 4": 15344},
    "Sample 4": {"Shelf 1": 44630, "Shelf 2": 38470, "Shelf 3": 27343, "Shelf 4": 19414},
    "Sample 5": {"Shelf 1": 45029, "Shelf 2": 41086, "Shelf 3": 31847, "Shelf 4": 22452},
}

# Calculate true count rates using the dead time correction
true_rates = {}
measured_rates = []  # Collecting measured rates for plotting
corrected_rates = []  # Collecting corrected rates for plotting

for sample, counts_per_shelf in sample_counts.items():
    true_rates[sample] = {}
    for shelf, count in counts_per_shelf.items():
        measured_rate = count / 10.0  # Convert to counts per second
        corrected_rate = measured_rate / (1 - (measured_rate * tau))  # Dead time correction formula

        # Storing results
        true_rates[sample][shelf] = corrected_rate
        measured_rates.append(measured_rate)
        corrected_rates.append(corrected_rate)

# Plotting measured vs. true count rates
plt.figure(figsize=(10, 6))
plt.scatter(measured_rates, corrected_rates, color='b', label='Measured vs. True Count Rates (Sample 6)')
plt.plot([0, max(measured_rates)], [0, max(measured_rates)], 'r--', label='Line of Equality')
plt.xlabel('Measured Count Rate (counts/s)')
plt.ylabel('True Count Rate (counts/s)')
plt.title('Measured vs. True Count Rates (Sample 6)')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('measured_vs_true_count_rates.png')