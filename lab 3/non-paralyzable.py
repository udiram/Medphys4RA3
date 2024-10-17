from scipy.stats import linregress
import matplotlib.pyplot as plt


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


# Define the relative activity (x) values for the samples
relative_activity = [1, 2, 3, 4, 5]  # Corresponding to Samples 1, 2, 3, 4, 5

# Prepare lists to store the 1/Cm and 1/x values for each shelf
inverse_cm = {f'Shelf {i+1}': [] for i in range(4)}
inverse_x = [1/x for x in relative_activity]

# Populate the lists for each shelf
for i in range(4):  # Loop over shelves 1 to 4
    for j, sample in enumerate(relative_activity):  # Loop over Samples 1 to 5
        cm_value = measured_count_rates[f'Sample {sample}'][i]
        inverse_cm[f'Shelf {i+1}'].append(1 / cm_value)

# Plot 1/Cm as a function of 1/x for each shelf and perform linear regression
shelf_dead_times = {}
plt.figure(figsize=(12, 8))
for shelf, cm_values in inverse_cm.items():
    # Perform linear regression to fit the line
    slope, intercept, _, _, _ = linregress(inverse_x, cm_values)
    shelf_dead_times[shelf] = slope  # Slope gives the dead time τ

    # Plot the data points and the fitted line
    plt.scatter(inverse_x, cm_values, label=f'{shelf} Data', alpha=0.7)
    plt.plot(inverse_x, [slope * x + intercept for x in inverse_x], label=f'{shelf} Fit', linestyle='--')

# Configure the plot
plt.xlabel('1/x (1/Relative Activity)')
plt.ylabel('1/Cm (1/Measured Count Rate)')
plt.title('1/Cm vs. 1/x for Each Shelf')
plt.legend()
plt.grid()
plt.savefig('1_cm_vs_1_x.png')
plt.show()

