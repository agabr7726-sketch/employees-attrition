import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("DEPI.csv", sep=";")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove columns that are not useful for modeling
# These columns are administrative/identifier-like in this dataset.
columns_to_drop = []

df = df.drop(columns=columns_to_drop)

# Save cleaned dataset
df.to_csv("DEPI_cleaned.csv", sep=";", index=False)

print("Cleaning completed successfully.")
print("Shape:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print("Duplicates:", df.duplicated().sum())