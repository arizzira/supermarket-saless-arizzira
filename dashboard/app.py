import os
import pandas as pd
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv
from sqlalchemy import create_engine

# 1. Page Configuration
st.set_page_config(
    page_title="Supermarket Sales Dashboard",
    layout="wide"
)

# 2. Database Connection (Local + Cloud Compatible)
# Prioritas: baca dari st.secrets (Cloud), fallback ke .env (Lokal)
try:
    DATABASE_URL = st.secrets["DATABASE_URL"]
except (KeyError, FileNotFoundError):
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

@st.cache_data
def load_data():
    """Fetch data from PostgreSQL and cache it for performance."""
    query = "SELECT * FROM sales;"
    return pd.read_sql_query(query, engine)

df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Data Filters")
selected_city = st.sidebar.multiselect(
    "Select City:",
    options=df["city"].unique(),
    default=df["city"].unique()
)

selected_category = st.sidebar.multiselect(
    "Select Product Category:",
    options=df["product_category"].unique(),
    default=df["product_category"].unique()
)

df_filtered = df[
    (df["city"].isin(selected_city)) &
    (df["product_category"].isin(selected_category))
]

# 4. Main Header
st.title("Supermarket Sales Dashboard")
st.markdown("Analysis of sales performance, customer behavior, and product contribution based on supermarket transaction data.")
st.divider()

# 5. KPI Metrics
total_revenue = df_filtered["total_price"].sum()
total_transactions = df_filtered["sale_id"].count()
avg_order_value = df_filtered["total_price"].mean()
member_pct = (df_filtered["is_member"].mean()) * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Transactions", f"{total_transactions:,}")
col3.metric("Avg Order Value", f"${avg_order_value:,.2f}")
col4.metric("Member Percentage", f"{member_pct:.1f}%")

st.divider()

# 6. Visualizations
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("Revenue by City")
    city_data = df_filtered.groupby("city")["total_price"].sum().reset_index()
    fig_city = px.bar(
        city_data,
        x="city",
        y="total_price",
        color="city",
        text_auto='.2s',
        color_discrete_sequence=px.colors.sequential.Blues_r
    )
    fig_city.update_layout(
        xaxis_title="City",
        yaxis_title="Total Revenue ($)",
        showlegend=False
    )
    st.plotly_chart(fig_city, use_container_width=True)

with row1_col2:
    st.subheader("Customer Type Distribution")
    member_data = df_filtered["customer_type"].value_counts().reset_index()
    member_data.columns = ["customer_type", "count"]
    fig_member = px.pie(
        member_data,
        names="customer_type",
        values="count",
        hole=0.4,
        color_discrete_sequence=["#1f77b4", "#ff7f0e"]
    )
    st.plotly_chart(fig_member, use_container_width=True)

st.subheader("Revenue by Product Category")
cat_data = df_filtered.groupby("product_category")["total_price"].sum().reset_index().sort_values("total_price", ascending=True)
fig_cat = px.bar(
    cat_data,
    x="total_price",
    y="product_category",
    orientation="h",
    text_auto='.2s',
    color="total_price",
    color_continuous_scale="Blues"
)
fig_cat.update_layout(
    xaxis_title="Total Revenue ($)",
    yaxis_title="Product Category",
    coloraxis_showscale=False
)
st.plotly_chart(fig_cat, use_container_width=True)