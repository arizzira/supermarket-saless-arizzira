DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    branch VARCHAR(1),
    city VARCHAR(50),
    customer_type VARCHAR(20),
    is_member BOOLEAN,
    gender VARCHAR(10),
    product_name VARCHAR(50),
    product_category VARCHAR(50),
    unit_price NUMERIC(10, 2),
    quantity INTEGER,
    tax NUMERIC(10, 2),
    total_price NUMERIC(10, 2),
    revenue_per_item NUMERIC(10, 2),
    reward_points INTEGER,
    reward_rate NUMERIC(10, 4),
    basket_size_segment VARCHAR(20),
    transaction_segment VARCHAR(20)
);

CREATE INDEX idx_sales_city ON sales(city);
CREATE INDEX idx_sales_branch ON sales(branch);
CREATE INDEX idx_sales_customer ON sales(customer_type);
CREATE INDEX idx_sales_product ON sales(product_name);
CREATE INDEX idx_sales_category ON sales(product_category);