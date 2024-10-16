import pandas as pd

# Creating the data for the table
data = {
    "Shelf": [5, 4, 3, 2],
    "Distance (cm)": [5.7, 4.3, 3.1, 1.7],
    "CPS": [2.89, 4.94, 9.13, 28.46],
    "Absolute Efficiency (%)": [2.65e-4, 4.53e-4, 8.38e-4, 2.61e-3],
    "Solid Angle (sr)": [0.024, 0.042, 0.082, 0.272],
    "Intrinsic Efficiency (%)": [1.39e-2, 1.19e-2, 1.13e-2, 1.21e-2]
}

# Converting the data to a DataFrame
df = pd.DataFrame(data)

# Saving the DataFrame to a CSV file
csv_file_path = "efficiencies_data.csv"
df.to_csv(csv_file_path, index=False)

# Displaying the DataFrame to the user
