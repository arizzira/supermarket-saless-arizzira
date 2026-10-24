import pandas as pd

df = pd.read_csv("data/raw/sales.csv")

print("=== SHAPE ===")
print(df.shape)

print("\n=== KOLOM ===")
print(df.columns.tolist())

print("\n=== 5 DATA PERTAMA ===")
print(df.head())

print("\n=== TIPE DATA ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== DUPLIKAT sale_id ===")
print(df["sale_id"].duplicated().sum())

print("\n=== STATISTIK NUMERIK ===")
print(df.describe())

print("\n=== NILAI UNIK PER KOLOM KATEGORI ===")
for col in ["branch", "city", "customer_type", "gender", "product_name", "product_category"]:
    print(f"{col}: {df[col].unique()}")