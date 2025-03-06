use retails_orders;
select * from df_orders1;
select * from df_orders2;


-- 1. Find top 10 highest revenue-generating products:
SELECT product_id, SUM(sale_price) AS sales
FROM df_orders2
GROUP BY product_id
ORDER BY sales DESC
LIMIT 10;

-- 2.  Find the top 5 cities with the highest profit margins
SELECT distinct(df_orders1.city),(df_orders2.profit) AS profit_margins 
FROM df_orders1
INNER JOIN df_orders2 ON df_orders1.sub_category = df_orders2.sub_category
LIMIT 5;


-- 3. Calculate the total discount given for each category
SELECT o1.category, SUM(o2.discount) AS total_discount
FROM df_orders1 o1
JOIN df_orders2 o2 ON o1.sub_category = o2.sub_category
GROUP BY o1.category;



 -- 4. Find the average sale price per product category
SELECT d1.category, AVG(d2.sale_price) AS avg_sale_price
FROM df_orders1 d1
JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category  -- Joining on sub_category
GROUP BY d1.category
ORDER BY avg_sale_price DESC
limit 5;


 -- 5.Find the region with the highest average sale price
SELECT d1.region, AVG(d2.sale_price) AS avg_sale_price
FROM df_orders1 d1
JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category  -- Joining on sub_category
GROUP BY d1.region
ORDER BY avg_sale_price DESC;



 -- 6. Find the total profit per category
SELECT d1.category, SUM(d2.profit) AS total_profit
FROM df_orders1 d1
JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category  -- Joining on sub_category
GROUP BY d1.category
ORDER BY total_profit DESC;


-- 7. dentify the top 3 segments with the highest quantity of orders
SELECT d1.segment, SUM(d2.quantity) AS total_quantity
FROM df_orders1 d1
JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category  -- Joining on sub_category
GROUP BY d1.segment
ORDER BY total_quantity DESC
LIMIT 3;

 
 -- 8. Determine the average discount percentage given per region
 SELECT d1.region, AVG(d2.discount_percent) AS avg_discount_percentage
FROM df_orders1 d1
JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category  -- Joining on sub_category
GROUP BY d1.region
ORDER BY avg_discount_percentage DESC;


-- 9. Find the product category with the highest total profit
SELECT d1.category, SUM(d2.profit) AS total_profit
FROM df_orders1 d1
JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category  -- Joining on sub_category
GROUP BY d1.category
ORDER BY total_profit DESC;



-- 10.Calculate the total revenue generated per year
SELECT YEAR(d1.order_date) AS year, 
       SUM(d2.sale_price) AS total_revenue
FROM df_orders1 d1
JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category  -- Join on common column
GROUP BY YEAR(d1.order_date)
ORDER BY year ASC;

-- 1. Get order details along with product pricing INNER JOIN 
SELECT o.order_id, o.order_date, o.city, o.state, p.product_id, p.sale_price, p.profit
FROM df_orders1 o
INNER JOIN df_orders2 p ON o.sub_category = p.sub_category;

-- 2.Get all orders and matching product details, if available LEFT JOIN 
SELECT o.order_id, o.order_date, o.city, p.product_id, p.sale_price, p.profit
FROM df_orders1 o
LEFT JOIN df_orders2 p ON o.sub_category = p.sub_category;

-- 3.Get all products and matching order details, if available RIGHT JOIN 
SELECT o.order_id, o.order_date, o.city, p.product_id, p.sale_price, p.profit
FROM df_orders1 o
RIGHT JOIN df_orders2 p ON o.sub_category = p.sub_category;

-- 4.Find Total Sales by Region using INNER JOIN
SELECT o.region, SUM(p.sale_price * p.quantity) AS total_sales
FROM df_orders1 o
INNER JOIN df_orders2 p ON o.sub_category = p.sub_category
GROUP BY o.region;


-- 5.Find Top 5 Most Profitable Products
SELECT product_id, sub_category, SUM(profit) AS total_profit
FROM df_orders2 
GROUP BY product_id, sub_category
ORDER BY total_profit DESC
LIMIT 5;

-- 6.Get Orders That Had a Discount Greater Than 20%  INNER JOIN 
SELECT o.order_id, o.order_date, p.product_id, p.discount_percent
FROM df_orders1 o
INNER JOIN df_orders2 p ON o.sub_category = p.sub_category
WHERE p.discount_percent > 20;

-- 7. Find Average Cost Price of Products for Each Category INNER JOIN 
SELECT o.category, AVG(p.cost_price) AS avg_cost_price
FROM df_orders1 o
INNER JOIN df_orders2 p ON o.sub_category = p.sub_category
GROUP BY o.category;

-- 8. Get Cities Where No Products Were Sold (Using LEFT JOIN and NULL check)
SELECT o.city, o.state
FROM df_orders1 o
LEFT JOIN df_orders2 p ON o.sub_category = p.sub_category
WHERE p.product_id IS NULL;

-- 9.Find the Total Profit by State
SELECT o.state, SUM(p.profit) AS total_profit
FROM df_orders1 o
INNER JOIN df_orders2 p ON o.sub_category = p.sub_category
GROUP BY o.state
ORDER BY total_profit DESC;


-- 10. Find Orders That Had Zero Profit
SELECT o.order_id, o.order_date, p.product_id, p.sale_price, p.profit
FROM df_orders1 o
INNER JOIN df_orders2 p ON o.sub_category = p.sub_category
WHERE p.profit = 0;















