
SELECT 
    city,
    COUNT(sale_id) AS total_transactions,
    ROUND(SUM(total_price), 2) AS total_revenue,
    ROUND(AVG(total_price), 2) AS avg_transaction_value,
    ROUND(AVG(quantity), 1) AS avg_basket_size
FROM sales
GROUP BY city
ORDER BY total_revenue DESC;

SELECT 
    city,
    COUNT(*) AS total_visitors,
    SUM(CASE WHEN is_member = TRUE THEN 1 ELSE 0 END) AS total_members,
    ROUND((SUM(CASE WHEN is_member = TRUE THEN 1 ELSE 0 END)::numeric / COUNT(*)) * 100, 1) AS member_percentage,
    ROUND((SUM(CASE WHEN gender = 'Male' THEN 1 ELSE 0 END)::numeric / COUNT(*)) * 100, 1) AS male_percentage,
    ROUND((SUM(CASE WHEN gender = 'Female' THEN 1 ELSE 0 END)::numeric / COUNT(*)) * 100, 1) AS female_percentage
FROM sales
GROUP BY city
ORDER BY member_percentage DESC;

SELECT 
    city,
    COUNT(CASE WHEN total_price > 100 THEN 1 END) AS big_spender_transactions,
    ROUND(AVG(reward_points), 1) AS avg_reward_points,
    ROUND(AVG(reward_rate), 4) AS avg_reward_rate
FROM sales
GROUP BY city
ORDER BY big_spender_transactions DESC;

SELECT 
    product_name,
    product_category,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(total_price), 2) AS total_revenue
FROM sales
GROUP BY product_name, product_category
ORDER BY total_revenue DESC;

SELECT city, product_category, total_revenue
FROM (
    SELECT 
        city, 
        product_category, 
        ROUND(SUM(total_price), 2) AS total_revenue,
        ROW_NUMBER() OVER (PARTITION BY city ORDER BY SUM(total_price) DESC) AS category_rank
    FROM sales
    GROUP BY city, product_category
) AS ranked
WHERE category_rank = 1;

SELECT 
    transaction_segment,
    basket_size_segment,
    COUNT(*) AS total_transactions,
    ROUND(AVG(total_price), 2) AS avg_revenue_per_transaction,
    ROUND(AVG(quantity), 1) AS avg_items_per_transaction
FROM sales
GROUP BY transaction_segment, basket_size_segment
ORDER BY avg_revenue_per_transaction DESC;