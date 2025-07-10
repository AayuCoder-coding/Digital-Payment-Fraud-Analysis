# 📊 Streamlit Dashboard for PhonePe Transaction Insights (National Level)

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PhonePe Insights", layout="wide", page_icon="📱")

# 📥 Load Data
@st.cache_data
def load_data():
    return pd.read_csv("final_aggregated_data.csv")

df = load_data()

# 🔍 Filters
years = sorted(df['year'].unique())
quarters = sorted(df['quarter'].unique())
year = st.sidebar.selectbox("Select Year", years)
quarter = st.sidebar.selectbox("Select Quarter", quarters)
filtered = df[(df['year'] == year) & (df['quarter'] == quarter)]

# 📢 Dashboard Header
st.title("📱 PhonePe UPI Transaction Dashboard (National Level)")
st.markdown("Analyzing UPI transaction trends in India using PhonePe Pulse data (2018–2024).")

# 📊 KPIs
col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Amount", f"₹{df['amount'].sum()/1e12:.2f} T")
col2.metric("🧾 Total Transactions", f"{df['count'].sum()/1e9:.2f} B")
col3.metric("🏆 Top Transaction Type", df.groupby("txn_type")["amount"].sum().idxmax())

st.markdown("---")

# 🥧 Pie Chart
st.subheader(f"🧾 {year} Q{quarter} – Transaction Type Share")
pie_data = filtered.groupby("txn_type").agg({'amount': 'sum'}).reset_index()
fig1 = px.pie(pie_data, names='txn_type', values='amount', title="Transaction Distribution")
st.plotly_chart(fig1, use_container_width=True)

# 📊 Bar Chart
st.subheader("🏆 All-Time Top Transaction Types")
bar_data = df.groupby("txn_type").agg({'amount': 'sum'}).reset_index().sort_values(by="amount", ascending=False)
fig2 = px.bar(bar_data, x='txn_type', y='amount', color='txn_type', title="Transaction Amount by Type")
st.plotly_chart(fig2, use_container_width=True)

# 📈 Trend Line
st.subheader("📈 Quarterly Growth Trend")
trend = df.groupby(['year', 'quarter']).agg({'amount': 'sum'}).reset_index()
trend['period'] = trend['year'].astype(str) + "-Q" + trend['quarter'].astype(str)
fig3 = px.line(trend, x='period', y='amount', markers=True, title="UPI Transaction Amount Over Time")
st.plotly_chart(fig3, use_container_width=True)

# 📄 Raw Data
st.subheader("📋 Filtered Data Table")
st.dataframe(filtered)

st.markdown("---")
st.markdown("Made with ❤️ by [Aayushi Verma]")

