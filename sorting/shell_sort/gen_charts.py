import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv("descending.csv", header=None)

# The first row contains the column headers (10, 100, 1000, 10000, 20000)
headers = data.iloc[0].tolist()
data = data[1:]  # Remove the header row from the data

# Convert the data to numeric values
data = data.apply(pd.to_numeric)

# Calculate the mean and standard deviation for each column
means = data.mean()
std_devs = data.std()

# Plotting the data as a bar chart
plt.figure(figsize=(10, 6))

# Create the bar chart
x_pos = np.arange(len(headers))  # X-axis positions for the bars
plt.bar(x_pos, means, yerr=std_devs, capsize=5, color="skyblue", label="Mean ± Std Dev")

# Adding labels and title
plt.xlabel("Data Points")
plt.ylabel("Time (seconds)")
plt.title("Performance Analysis (Descending)")
plt.xticks(x_pos, headers)  # Set x-axis labels to the headers (10, 100, 1000, etc.)
plt.legend()

# Add gridlines for better readability
plt.grid(True, axis="y")

# Save the plot as an image file
plt.savefig(
    "descending.png", dpi=300, bbox_inches="tight"
)  # Save as PNG with high resolution

# Optionally, display the plot as well
plt.show()
