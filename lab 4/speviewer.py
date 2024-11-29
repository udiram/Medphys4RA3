import matplotlib.pyplot as plt
import numpy as np

# Load the file and display first few lines to understand its structure
file_path = 'background.Spe'

with open(file_path, 'r') as file:
    lines = file.readlines()



# Extract data section starting from the `$DATA` marker
data_start = lines.index('$DATA:\n') + 2  # Skip the '$DATA:' line and range line
data_values = [int(line.strip()) for line in lines[data_start:data_start + 1024]]

# Generate channels and plot
channels = np.arange(len(data_values))

# Apply the conversion formula to channels to get energy values
energy_values = 5.25 * channels - 404.14

# Plot with energy on the x-axis
plt.figure(figsize=(10, 6))
plt.plot(energy_values, data_values, label='Counts vs Energy')
plt.xlabel('Energy (keV)')
plt.ylabel('Counts')
plt.title('Spectral Data Visualization (Energy Scale)')
plt.legend()
plt.grid(True)
plt.savefig('background.png', dpi=1000)
plt.show()

