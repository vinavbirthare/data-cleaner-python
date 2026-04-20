import pandas as pd

file_name = input("Enter your CSV file name (with .csv): ")

df = pd.read_csv(file_name)

print("\nOriginal Data:")
print(df)

df = df.drop_duplicates()
df = df.fillna("N/A")

output_file = "cleaned_" + file_name
df.to_csv(output_file, index=False)

print(f"\nData cleaned successfully! Saved as {output_file}")