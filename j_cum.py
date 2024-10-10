import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Re-create the data from the image into a pandas DataFrame
data = {
    'Event Interval': ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13', '13-14', '14-15',
                       '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22', '22-23', '23-24', '24-25', '23-26', '26-27', '27-28',
                       '28-29', '29-30', '30-31', '31-32', '32-33', '33-34', '34-35', '35-36', '36-37', '37-38', '38-39', '39-40', '40-41',
                       '41-42', '42-43', '43-44', '44-45', '45-46', '46-47', '47-48', '48-49', '49-50'],
    'Time Interval (ms)': [415, 87, 421, 128, 356, 208, 1018, 414, 108, 142, 381, 1284, 43, 449, 122, 189, 26, 184, 530, 613, 526, 247,
                           985, 390, 280, 77, 327, 602, 441, 224, 371, 57, 700, 1456, 116, 57, 305, 476, 95, 357, 3, 101, 123, 555,
                           468, 715, 205, 654, 852, 144]
}

df = pd.DataFrame(data)

# Extract time intervals from the DataFrame
time_intervals_new = df['Time Interval (ms)']

# Recalculate the mean count rate based on the new data
mean_count_rate_new = 1 / np.mean(time_intervals_new / 1000)  # Convert ms to seconds

# Define the Poisson model function for theoretical curve
def poisson_model(t, C):
    return C * np.exp(-C * t)

# Time intervals for theoretical curve (in seconds)
t_values_new = np.linspace(0, max(time_intervals_new) / 1000, 500)

# Theoretical curve
theoretical_curve_new = poisson_model(t_values_new, mean_count_rate_new)

# Cumulative time interval distribution
time_intervals_sorted = np.sort(time_intervals_new / 1000)
cumulative_values = np.arange(1, len(time_intervals_sorted) + 1) / len(time_intervals_sorted)

# Plot cumulative distribution and theoretical Poisson curve
plt.figure(figsize=(10, 6))
plt.step(time_intervals_sorted, cumulative_values, where='post', label="Cumulative Experimental Data", alpha=0.6)
plt.plot(t_values_new, 1 - np.exp(-mean_count_rate_new * t_values_new), color='red', label="Poisson Theoretical CDF")

# Add labels and title
plt.xlabel('Time Interval (s)')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Time Interval Distribution with Theoretical Poisson CDF (New Data)')
plt.legend()

# Show the plot
plt.show()