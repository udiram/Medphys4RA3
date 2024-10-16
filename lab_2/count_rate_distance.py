import matplotlib.pyplot as plt
import pandas as pd

# Data for count rate (cps) and distance (cm)
shelf_data = {
    "Shelf": [5, 4, 3, 2],
    "Counts": [289, 494, 913, 2846],
    "cps": [2.89, 4.94, 9.13, 24.46],
    "Distance (cm)": [5.7, 4.3, 3.1, 1.7]
}

# Convert data into a DataFrame
df_shelf = pd.DataFrame(shelf_data)

# Re-plotting with the x-axis correctly going from low to high (no inversion)
plt.figure(figsize=(8, 6))
plt.plot(df_shelf["Distance (cm)"], df_shelf["cps"], 'bo', label='Count Rate Data', markersize=8)  # Discrete points
plt.xlabel('Distance to Surface of Detector (cm)')
plt.ylabel('Count Rate (cps)')
plt.title('Count Rate vs Source-Detector Distance (Discrete)')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
