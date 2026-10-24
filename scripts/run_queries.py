import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def run_query(sql_query, title):
    """Fungsi untuk menjalankan query dan print hasilnya dengan rapi"""
    print(f"\n{'='*50}")
    print(f"📊 {title}")
    print(f"{'='*50}")
    
    with engine.connect() as conn:
        df = pd.read_sql_query(text(sql_query), conn)
    
    print(df.to_string(index=False))
    return df


query_revenue = """
SELECT city, COUNT(sale_id) AS total_transactions, 
       ROUND(SUM(total_price), 2) AS total_revenue 
FROM sales GROUP BY city ORDER BY total_revenue DESC;
"""
run_query(query_revenue, "Revenue per City")

query_loyalty = """
SELECT city, 
       ROUND((SUM(CASE WHEN is_member = TRUE THEN 1 ELSE 0 END)::numeric / COUNT(*)) * 100, 1) AS member_percentage
FROM sales GROUP BY city ORDER BY member_percentage DESC;
"""
run_query(query_loyalty, "Member Percentage per City")

query_top_product = """
SELECT product_name, ROUND(SUM(total_price), 2) AS total_revenue
FROM sales GROUP BY product_name ORDER BY total_revenue DESC LIMIT 3;
"""
run_query(query_top_product, "Top 3 Products by Revenue")