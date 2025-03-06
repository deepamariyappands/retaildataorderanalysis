import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Database credentials (Update with your actual details)
DB_USER = "root"
DB_PASSWORD = "8524837656"
DB_HOST = "127.0.0.1"  # e.g., "localhost" or an IP
DB_PORT = "3306"  # Default MySQL port
DB_NAME = "retails_orders"

# Create MySQL connection
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# Define SQL queries
queries_page1 = {
    "Top 10 Revenue-Generating Products": """
        SELECT product_id, SUM(sale_price) AS sales
        FROM df_orders2
        GROUP BY product_id
        ORDER BY sales DESC
        LIMIT 10;
    """,
    "Top 5 Cities with Highest Profit Margins": """
        SELECT df_orders1.city, SUM(df_orders2.profit) AS profit_margins 
        FROM df_orders1
        INNER JOIN df_orders2 ON df_orders1.sub_category = df_orders2.sub_category
        GROUP BY df_orders1.city
        ORDER BY profit_margins DESC
        LIMIT 5;
    """,
    "Total Discount Given for Each Category": """
        SELECT o1.category, SUM(o2.discount) AS total_discount
        FROM df_orders1 o1
        JOIN df_orders2 o2 ON o1.sub_category = o2.sub_category
        GROUP BY o1.category;
    """,
    "Total Revenue Generated per Year": """
        SELECT YEAR(d1.order_date) AS year, 
               SUM(d2.sale_price) AS total_revenue
        FROM df_orders1 d1
        JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category
        GROUP BY YEAR(d1.order_date)
        ORDER BY year ASC;
    """,
    "Find the region with the highest average sale price": """
        SELECT d1.region, AVG(d2.sale_price) AS avg_sale_price
        FROM df_orders1 d1
        JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category
        GROUP BY d1.region
        ORDER BY avg_sale_price DESC;
    """,
    "Find the total profit per category": """
        SELECT d1.category, SUM(d2.profit) AS total_profit
        FROM df_orders1 d1
        JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category
        GROUP BY d1.category
        ORDER BY total_profit DESC;
    """,
    "Identify the top 3 segments with the highest quantity of orders": """
        SELECT d1.segment, SUM(d2.quantity) AS total_quantity
        FROM df_orders1 d1
        JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category
        GROUP BY d1.segment
        ORDER BY total_quantity DESC
        LIMIT 3;
    """,
    "Determine the average discount percentage given per region": """
        SELECT d1.region, AVG(d2.discount_percent) AS avg_discount_percentage
        FROM df_orders1 d1
        JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category
        GROUP BY d1.region
        ORDER BY avg_discount_percentage DESC;
    """,
    "Find the product category with the highest total profit": """
        SELECT d1.category, SUM(d2.profit) AS total_profit
        FROM df_orders1 d1
        JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category
        GROUP BY d1.category
        ORDER BY total_profit DESC;
    """,
    "Calculate the total revenue generated per year": """
        SELECT YEAR(d1.order_date) AS year, 
               SUM(d2.sale_price) AS total_revenue
        FROM df_orders1 d1
        JOIN df_orders2 d2 ON d1.sub_category = d2.sub_category
        GROUP BY YEAR(d1.order_date)
        ORDER BY year ASC;
    """
}

queries_page2 = {
    "Order Details with Product Pricing": """
        SELECT o.order_id, o.order_date, o.city, o.state, p.product_id, p.sale_price, p.profit
        FROM df_orders1 o
        INNER JOIN df_orders2 p ON o.sub_category = p.sub_category;
    """,
    
    "All Orders and Matching Product Details ": """
        SELECT o.order_id, o.order_date, o.city, o.state, p.product_id, p.sale_price, p.profit
        FROM df_orders1 o
        LEFT JOIN df_orders2 p ON o.sub_category = p.sub_category;
    """,
    
    "Top 5 Most Profitable Products": """
        SELECT p.product_id, o.sub_category, SUM(p.profit) AS total_profit
        FROM df_orders1 o
        INNER JOIN df_orders2 p ON o.sub_category = p.sub_category
        GROUP BY p.product_id, o.sub_category
        ORDER BY total_profit DESC
        LIMIT 5;
    """,
    
    "Orders with Zero Profit": """
        SELECT o.order_id, o.order_date, o.city, o.state, p.product_id, p.sale_price, p.profit
        FROM df_orders1 o
        INNER JOIN df_orders2 p ON o.sub_category = p.sub_category
        WHERE p.profit = 0;
    """,
    
    "Total Sales and Profit by Region": """
        SELECT o.region, SUM(p.sale_price) AS total_sales, SUM(p.profit) AS total_profit
        FROM df_orders1 o
        INNER JOIN df_orders2 p ON o.sub_category = p.sub_category
        GROUP BY o.region
        ORDER BY total_sales DESC;
    """,
    
    "Average Discount Percentage by Category": """
        SELECT o.category, AVG(p.discount_percent) AS avg_discount_percentage
        FROM df_orders1 o
        INNER JOIN df_orders2 p ON o.sub_category = p.sub_category
        GROUP BY o.category
        ORDER BY avg_discount_percentage DESC;
    """,
    
    "Total Quantity Sold per Product": """
        SELECT p.product_id, SUM(p.quantity) AS total_quantity
        FROM df_orders1 o
        INNER JOIN df_orders2 p ON o.sub_category = p.sub_category
        GROUP BY p.product_id
        ORDER BY total_quantity DESC;
    """,
    
    "Orders with Highest Discount Applied": """
        SELECT o.order_id, o.order_date, o.city, o.state, p.product_id, p.discount
        FROM df_orders1 o
        INNER JOIN df_orders2 p ON o.sub_category = p.sub_category
        ORDER BY p.discount DESC
        LIMIT 10;
    """,
    
    "Top 5 Most Ordered Sub-Categories": """
        SELECT o.sub_category, SUM(p.quantity) AS total_orders
        FROM df_orders1 o
        INNER JOIN df_orders2 p ON o.sub_category = p.sub_category
        GROUP BY o.sub_category
        ORDER BY total_orders DESC
        LIMIT 5;
    """,
    
    "Revenue and Profit Per Year": """
        SELECT YEAR(o.order_date) AS year, SUM(p.sale_price) AS total_revenue, SUM(p.profit) AS total_profit
        FROM df_orders1 o
        INNER JOIN df_orders2 p ON o.sub_category = p.sub_category
        GROUP BY YEAR(o.order_date)
        ORDER BY year ASC;
    """
}


# Streamlit UI
st.title("📊 Retail Orders Data Analysis")

# Create tabs for two pages
tab1, tab2 = st.tabs(["Query Set 1", "Query Set 2"])

# Page 1: First Set of Queries
with tab1:
    st.header("🔍 Data Insights")
    selected_query = st.selectbox("Select a Query to Run:", list(queries_page1.keys()), key="page1")
    if st.button("Run Query", key="run1"):
        try:
            with engine.connect() as connection:
                df = pd.read_sql(queries_page1[selected_query], connection)
                st.write(f"### Results for: {selected_query}")
                st.dataframe(df)
        except Exception as e:
            st.error(f"Query failed: {e}")

# Page 2: Second Set of Queries
with tab2:
    st.header("🔍 Data Insights ")
    selected_query2 = st.selectbox("Select a Query to Run:", list(queries_page2.keys()), key="page2")
    if st.button("Run Query", key="run2"):
        try:
            with engine.connect() as connection:
                df = pd.read_sql(queries_page2[selected_query2], connection)
                st.write(f"### Results for: {selected_query2}")
                st.dataframe(df)
        except Exception as e:
            st.error(f"Query failed: {e}")
