import matplotlib.pyplot as plt
import numpy as np

# Example data for measured count rates (per second), representing each shelf for samples 1-6
measured_count_rates = {
    'Sample 1': [33891, 16946, 9431, 6002],  # Shelves 1 to 4
    'Sample 2': [41940, 27330, 16700, 11202],
    'Sample 3': [43895, 33848, 22331, 15344],
    'Sample 4': [44630, 38470, 27343, 19414],
    'Sample 5': [45029, 41086, 31847, 22452],
    'Sample 6': [1938, 664, 341, 216]       # Calibration sample, assumed true
}

# Assume a dead time value τ (in seconds) estimated from previous analysis
dead_time = 1.5e-5  # 15 microseconds as an example

# Calculate the true count rates for all samples using the dead time correction formula
true_count_rates = {}
for sample, counts in measured_count_rates.items():
    true_counts = [cm / (1 - cm * dead_time) for cm in counts]
    true_count_rates[sample] = true_counts

# Prepare data for plotting
measured_rates = []
true_rates = []
for sample in measured_count_rates:
    if sample != 'Sample 6':  # Exclude Sample 6 as it's used as the calibration reference
        measured_rates.extend(measured_count_rates[sample])
        true_rates.extend(true_count_rates[sample])

# Plot measured count rate vs. true count rate
plt.figure(figsize=(10, 6))
plt.scatter(measured_rates, true_rates, label='Samples 1-5', color='blue')
plt.plot([0, max(measured_rates)], [0, max(measured_rates)], 'r--', label='Line of Equality')
plt.xlabel('Measured Count Rate (counts/sec)')
plt.ylabel('True Count Rate (counts/sec)')
plt.title('Measured Count Rate vs. True Count Rate')
plt.legend()
plt.grid()
plt.savefig('measured_vs_true_count_rate.png')
plt.show()
