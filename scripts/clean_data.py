"""
clean_data.py
=============
Membersihkan & memperkaya dataset supermarket sales.

Input : data/raw/sales.csv
Output: data/processed/sales_clean.csv

Yang dilakukan:
1. Standarkan nama kolom (snake_case)
2. Validasi integritas (cek rumus bisnis konsisten)
3. Feature engineering (kolom turunan analitis)
4. Simpan ke processed/
"""

from pathlib import Path
import pandas as pd
import numpy as np

RAW = Path("data/raw/sales.csv")
OUT = Path("data/processed/sales_clean.csv")
OUT.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(RAW)
print(f"[LOAD] {len(df)} baris, {len(df.columns)} kolom")

df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
)

print("\n[VALIDATION] Cek konsistensi rumus bisnis...")

calc_total = (df["unit_price"] * df["quantity"] + df["tax"]).round(2)
mismatch_total = (calc_total - df["total_price"]).abs() > 0.02
print(f"  - total_price mismatch : {mismatch_total.sum()} / {len(df)}")

subtotal = df["unit_price"] * df["quantity"]
calc_tax = (subtotal * 0.07).round(2)
mismatch_tax = (calc_tax - df["tax"]).abs() > 0.02
print(f"  - tax mismatch (~7%)   : {mismatch_tax.sum()} / {len(df)}")

calc_reward = np.where(
    df["customer_type"] == "Member",
    np.floor(df["total_price"] / 10).astype(int),
    0,
)
mismatch_reward = calc_reward != df["reward_points"]
print(f"  - reward mismatch      : {mismatch_reward.sum()} / {len(df)}")


print("\n[FEATURE ENGINEERING] Tambah kolom turunan...")

df["is_member"] = df["customer_type"].eq("Member")

df["revenue_per_item"] = (df["total_price"] / df["quantity"]).round(2)

df["reward_rate"] = np.where(
    df["is_member"] & (df["total_price"] > 0),
    df["reward_points"] / df["total_price"],
    0.0,
).round(4)

df["basket_size_segment"] = pd.cut(
    df["quantity"],
    bins=[0, 5, 12, float("inf")],
    labels=["Small", "Medium", "Large"],
)

df["transaction_segment"] = pd.cut(
    df["total_price"],
    bins=[0, 50, 150, float("inf")],
    labels=["Low", "Medium", "High"],
)

final_cols = [
    "sale_id", "branch", "city",
    "customer_type", "is_member", "gender",
    "product_name", "product_category",
    "unit_price", "quantity", "tax",
    "total_price", "revenue_per_item",
    "reward_points", "reward_rate",
    "basket_size_segment", "transaction_segment",
]
df = df[final_cols]

df.to_csv(OUT, index=False)
print(f"\n[SAVE] Disimpan ke: {OUT}")
print(f"[DONE] {len(df)} baris, {len(df.columns)} kolom")

print("\n[PREVIEW] 3 baris terakhir:")
print(df.tail(3).to_string())