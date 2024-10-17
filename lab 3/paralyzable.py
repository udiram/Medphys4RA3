import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Data from the lab report - measured counts for different shelves (assuming average values where necessary)
# The values need to be provided here to proceed with plotting and fitting

# Example data based on the shelf counts provided in the document for each sample (shelves 1 to 4)
shelf_counts = {
    'shelf1': [41940, 33891, 43995, 45029, 44630],  # Example counts for each sample
    'shelf2': [27330, 16946, 41086, 38470],         # Example counts for each sample
    'shelf3': [16700, 9431, 31847, 27343],          # Example counts for each sample
    'shelf4': [11202, 6002, 22452, 19414]           # Example counts for each sample
}

# Relative activities for each sample compared to sample 1
relative_activity = np.array([1, 2, 3, 4, 5])

# Placeholder for calculating ln(Cm/x) and fitting a line to get dead time
shelf_lnCm_over_x = {}

# Loop over each shelf and calculate ln(Cm/x)
for shelf, counts in shelf_counts.items():
    lnCm_over_x = np.log(np.array(counts) / relative_activity[:len(counts)])
    shelf_lnCm_over_x[shelf] = lnCm_over_x

    # Fit ln(Cm/x) as a function of x (relative activity)
    slope, intercept, r_value, p_value, std_err = linregress(relative_activity[:len(counts)], lnCm_over_x)

    # Calculate dead time (tau) from the slope using the paralyzable model
    tau = -1 / slope

    # Plot the data and the fitted line
    plt.figure()
    plt.scatter(relative_activity[:len(counts)], lnCm_over_x, label=f'Data ({shelf})')
    plt.plot(relative_activity[:len(counts)], slope * relative_activity[:len(counts)] + intercept,
             label=f'Fit: slope={slope:.2f}, intercept={intercept:.2f}\nτ={tau:.2e}s', color='red')
    plt.xlabel('Relative Activity (x)')
    plt.ylabel('ln(Cm/x)')
    plt.title(f'ln(Cm/x) vs. x for {shelf}')
    plt.legend()
    plt.grid()
    plt.show()

    print(f"For {shelf}, the estimated dead time τ is {tau:.2e} seconds.")
