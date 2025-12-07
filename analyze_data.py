import pandas as pd

# ---- Load Data ----
df = pd.read_csv("data/your_dataset.csv")

print("\n=== FIRST FIVE ROWS ===")
print(df.head())

print("\n=== INFO ===")
print(df.info())

print("\n=== DESCRIBE ===")
print(df.describe())

# ---- Indexing with loc and iloc ----

print("\n=== SINGLE ROW BY LABEL (loc) ===")
print(df.loc[0])

print("\n=== SINGLE ROW BY POSITION (iloc) ===")
print(df.iloc[0])

print("\n=== ROW SLICE BY LABEL (loc) ===")
print(df.loc[0:3])

print("\n=== ROW SLICE BY POSITION (iloc) ===")
print(df.iloc[0:3])

print("\n=== SINGLE COLUMN BY NAME (Value) ===")
print(df["Value"].head())

print("\n=== SINGLE CELL BY LABELS (row 0, column 'Value') ===")
print(df.loc[0, "Value"])

# ---- Boolean Filtering ----

print("\n=== FILTER: SINGLE CONDITION (Value > 12) ===")
filtered1 = df[df["Value"] > 12]
print(filtered1.head())

print("\n=== FILTER: MULTIPLE CONDITIONS (Value > 10 AND Category == 'A') ===")
filtered2 = df[(df["Value"] > 10) & (df["Category"] == "A")]
print(filtered2.head())

# ---- Add and Remove Columns ----

print("\n=== ADDING NEW COLUMN (DoubleValue = Value * 2) ===")
df["DoubleValue"] = df["Value"] * 2
print(df[["Value", "DoubleValue"]].head())

print("\n=== DROPPING COLUMN (DoubleValue) ===")
df = df.drop(columns=["DoubleValue"])
print(df.columns)

# ---- GroupBy Operation ----

print("\n=== GROUPBY Category → Mean Score ===")
grouped = df.groupby("Category")["Score"].mean()
print(grouped)

print("\nAnalysis complete.")
