
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("clinic_data.csv")

# Title
st.title("Clinic Financial Performance Dashboard")

# Display raw data
with st.expander("📄 View Raw Data"):
    st.dataframe(df)

# KPIs
st.subheader("🔍 Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${df['Total_Revenue'].sum():,.0f}")
col2.metric("Total Expenses", f"${df['Total_Expenses'].sum():,.0f}")
col3.metric("Net Profit", f"${df['Net_Profit'].sum():,.0f}")

# Charts
st.subheader("📊 Monthly Trends")

# Line chart for Revenue and Expenses
fig, ax = plt.subplots()
ax.plot(df['Month'], df['Total_Revenue'], label='Total Revenue', marker='o')
ax.plot(df['Month'], df['Total_Expenses'], label='Total Expenses', marker='o')
ax.plot(df['Month'], df['Net_Profit'], label='Net Profit', marker='o')
ax.set_xlabel("Month")
ax.set_ylabel("Amount ($)")
ax.set_title("Revenue, Expenses, and Net Profit Over Time")
ax.legend()
st.pyplot(fig)

# Bar chart for Patient Volume
st.subheader("👥 Patient Volume")
st.bar_chart(df.set_index('Month')['Patients'])

# Avg Revenue per Patient
st.subheader("📈 Average Revenue per Patient")
st.line_chart(df.set_index('Month')['Avg_Revenue_per_Patient'])

st.markdown("**Built by Ndaale Ansah**")
