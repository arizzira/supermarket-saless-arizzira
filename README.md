# Supermarket Sales Analysis and Interactive Dashboard

An end-to-end data analysis portfolio project designed to evaluate supermarket sales performance, customer behavior, and product contributions. This project demonstrates a complete data pipeline, from data cleaning and database management to SQL analysis, data visualization, and interactive dashboard deployment.

## Business Questions

1. Which city generates the highest total revenue?
2. Which products and categories contribute most significantly to sales?
3. What is the behavioral comparison between Member and Normal customers?
4. How are transactions segmented based on basket size and transaction value?

## Tech Stack

- **Programming Language:** Python
- **Data Manipulation:** Pandas, NumPy
- **Database:** PostgreSQL
- **Database Toolkit:** SQLAlchemy
- **Data Visualization:** Matplotlib, Seaborn, Plotly
- **Dashboard Framework:** Streamlit
- **Version Control:** Git, GitHub

## Dataset Overview

The dataset used is the Supermarket Sales Dataset, consisting of 1,000 transaction records. 
*Note: This dataset is synthetic and does not include temporal dimensions (date/time) or payment methods. Therefore, the analysis focuses on demographic performance, product performance, and customer loyalty.*

## Data Pipeline

1. **Data Cleaning & Feature Engineering:** Standardized column names, validated business logic formulas (tax, total price, reward points), and engineered new features (`is_member`, `transaction_segment`, `basket_size_segment`, `reward_rate`).
2. **Database Integration:** Designed a relational schema in PostgreSQL and loaded the cleaned dataset using `psql \copy`.
3. **SQL Analysis:** Executed advanced SQL queries (including Window Functions) to answer key business questions.
4. **Exploratory Data Analysis (EDA):** Generated statistical visualizations using Matplotlib and Seaborn to uncover trends.
5. **Interactive Dashboard:** Developed a dynamic web application using Streamlit and Plotly, allowing users to filter data by city and product category.

## Key Insights

- **City Performance:** Chicago generates the highest total revenue (~$42.5k) despite having fewer transactions than New York. This indicates that customers in Chicago have a higher Average Order Value (AOV).
- **Product Contribution:** The "Personal Care" category is the largest revenue driver ($27k), followed closely by "Fruits" and "Beverages".
- **Customer Loyalty:** The customer base is nearly evenly split, with **51.6% Members** and 48.4% Normal customers. Members show a consistent pattern of higher transaction values due to the reward points system.

## Dashboard Preview

![Dashboard Preview](docs/dashboard.png)

## How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/[Your GitHub Username]/portfolio-supermarket-sales.git
   cd portfolio-supermarket-sales# Supermarket Sales Analysis and Interactive Dashboard

An end-to-end data analysis portfolio project designed to evaluate supermarket sales performance, customer behavior, and product contributions. This project demonstrates a complete data pipeline, from data cleaning and database management to SQL analysis, data visualization, and interactive dashboard deployment.

## Business Questions

1. Which city generates the highest total revenue?
2. Which products and categories contribute most significantly to sales?
3. What is the behavioral comparison between Member and Normal customers?
4. How are transactions segmented based on basket size and transaction value?

## Tech Stack

- Programming Language: Python
- Data Manipulation: Pandas, NumPy
- Database: PostgreSQL
- Database Toolkit: SQLAlchemy
- Data Visualization: Matplotlib, Seaborn, Plotly
- Dashboard Framework: Streamlit
- Version Control: Git, GitHub

## Dataset Overview

The dataset used is the Supermarket Sales Dataset, consisting of 1,000 transaction records. 
Note: This dataset is synthetic and does not include temporal dimensions (date/time) or payment methods. Therefore, the analysis focuses on demographic performance, product performance, and customer loyalty.

## Data Pipeline

1. Data Cleaning & Feature Engineering: Standardized column names, validated business logic formulas (tax, total price, reward points), and engineered new features (is_member, transaction_segment, basket_size_segment, reward_rate).
2. Database Integration: Designed a relational schema in PostgreSQL and loaded the cleaned dataset using psql \copy.
3. SQL Analysis: Executed advanced SQL queries (including Window Functions) to answer key business questions.
4. Exploratory Data Analysis (EDA): Generated statistical visualizations using Matplotlib and Seaborn to uncover trends.
5. Interactive Dashboard: Developed a dynamic web application using Streamlit and Plotly, allowing users to filter data by city and product category.

## Key Insights

- City Performance: Chicago generates the highest total revenue (~$42.5k) despite having fewer transactions than New York. This indicates that customers in Chicago have a higher Average Order Value (AOV).
- Product Contribution: The "Personal Care" category is the largest revenue driver ($27k), followed closely by "Fruits" and "Beverages".
- Customer Loyalty: The customer base is nearly evenly split, with 51.6% Members and 48.4% Normal customers. Members show a consistent pattern of higher transaction values due to the reward points system.

## Dashboard Preview

![Dashboard Preview](docs/dashboard.png)

## How to Run Locally

1. Clone the repository

git clone https://github.com/arizzira/portfolio-supermarket-sales.git
cd portfolio-supermarket-sales

2. Set up a virtual environment and install dependencies

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3. Database Configuration
- Create a new PostgreSQL database named portfolio_sales.
- Create a .env file in the root directory and add your database credentials:

DATABASE_URL=postgresql+psycopg2://portfolio_sales:arizganteng@localhost:5432/portfolio_sales

4. Execute Data Pipeline

# Clean and process raw data
python scripts/clean_data.py

# Create database schema
psql -U ariz -d portfolio_sales -f sql/create_table.sql

# Load data into PostgreSQL
psql -U ariz -d portfolio_sales -c "\copy sales FROM 'data/processed/sales_clean.csv' DELIMITER ',' CSV HEADER;"

5. Launch the Dashboard

streamlit run dashboard/app.py

---
Developed by Ariz as part of a Data Analyst Portfolio.