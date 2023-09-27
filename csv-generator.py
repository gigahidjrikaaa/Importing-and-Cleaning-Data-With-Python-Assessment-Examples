import pandas as pd
import numpy as np
import csv

# Define the data as a list of dictionaries
data = [
    {"id": 1, "name": "Ann", "team": "Bosses"},
    {"id": 2, "name": "Bob", "team": "Champions"},
    {"id": 3, "name": "Fred", "team": "Bosses"},
    {"id": 4, "name": "Chuck", "team": "Champions"},
]

# Define the CSV file path
csv_file_path = "data.csv"

# Define the CSV column headers
csv_columns = ["id", "name", "team"]

# Write the data to the CSV file
with open(csv_file_path, "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    
    # Write the header row
    writer.writeheader()
    
    # Write the data rows
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' has been created.")
