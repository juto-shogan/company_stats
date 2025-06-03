import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="EDA Assignment 2", layout="wide")
st.title("📊 EDA Task App - Assignment 2")

st.sidebar.header("Upload Dataset")
df = pd.read_csv('data/data.csv')

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.sidebar.header("Select EDA Task")
task = st.sidebar.selectbox("Choose an analysis to perform:", [
    "Trend of total sales and profits over time",
    "Sales and profits comparison by state",
    "Discount vs Profit scatter plot",
    "Distribution of ship modes",
    "Top 5 customers (sales, profit, discount)",
    "Sales and profit map by state",
    "Customer loyalty analysis (order frequency)",
    "Top 10 selling products",
    "Predominant subcategory in terms of sales",
    "Correlation between discount, sales, and profit"
])

if task == "Trend of total sales and profits over time":
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    trend = df.groupby(df['Order Date'].dt.to_period("M")).agg({"Sales": "sum", "Profit": "sum"})
    trend.index = trend.index.to_timestamp()
    trend = trend.reset_index()
    fig = px.line(trend, x='Order Date', y=['Sales', 'Profit'], title="Monthly Sales and Profit Trends")
    st.plotly_chart(fig)

elif task == "Sales and profits comparison by state":
    state_data = df.groupby("State")[['Sales', 'Profit']].sum().reset_index()
    fig = px.bar(state_data, x='State', y=['Sales', 'Profit'], barmode='group', title="Sales and Profit by State")
    st.plotly_chart(fig)

elif task == "Discount vs Profit scatter plot":
    fig = px.scatter(df, x="Discount", y="Profit", title="Discount vs Profit")
    st.plotly_chart(fig)

elif task == "Distribution of ship modes": 
    mode_counts = df['Ship Mode'].value_counts().reset_index()
    mode_counts.columns = ['Ship Mode', 'Count']
    fig = px.bar(mode_counts, x='Ship Mode', y='Count', title="Distribution of Ship Modes")
    st.plotly_chart(fig) 

elif task == "Top 5 customers (sales, profit, discount)": 
    top_customers = df.groupby('Customer Name')[['Sales', 'Profit', 'Discount']].sum().reset_index()
    top_customers = top_customers.sort_values("Sales", ascending=False).head(5)
    fig = px.bar(top_customers, x='Customer Name', y=['Sales', 'Profit', 'Discount'], barmode='group', title="Top 5 Customers")
    st.plotly_chart(fig) 

elif task == "Sales and profit map by state":
    st.warning("Map plotting requires geolocation data. This is a placeholder.")

elif task == "Customer loyalty analysis (order frequency)": 
    customer_orders = df['Customer Name'].value_counts().head(10).reset_index()
    customer_orders.columns = ['Customer Name', 'Order Count']
    fig = px.bar(customer_orders, x='Customer Name', y='Order Count', title="Top 10 Loyal Customers")
    st.plotly_chart(fig) 

elif task == "Top 10 selling products": 
    top_products = df.groupby('Product Name')["Sales"].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.bar(top_products, x='Product Name', y='Sales', title="Top 10 Selling Products")
    st.plotly_chart(fig) 

elif task == "Predominant subcategory in terms of sales":
    number_sub_cat = df['Sub-Category'].nunique()
    sub_category_counts = df['Sub-Category'].value_counts()
    sub_category_counts_sorted = sub_category_counts.sort_values(ascending=False)

    predominant_category = sub_category_counts_sorted.index[0]
    second_predominant = sub_category_counts_sorted.index[1]
    
    st.write("Number of categories:",number_sub_cat)
    st.write(f"Predominant Sub-Category: {predominant_category}")
    st.write(f"Second Predominant Sub-Category: {second_predominant}")

    predominant_subcategory = df.groupby('Sub-Category')['Sales'].sum().idxmax()
    st.write(f"The predominant subcategory in terms of sales is: {predominant_subcategory}")

elif task == "Correlation between discount, sales, and profit": 
    correlation = df[['Discount', 'Sales', 'Profit']].corr()
    fig = px.imshow(correlation, text_auto=True, title="Correlation Matrix")
    st.plotly_chart(fig) 