import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# Load dataset
df = sns.load_dataset("tips")

# Title and description
st.title("Tips Dataset Dashboard")
st.markdown("""
Explore how variables like gender, day, total bill, and more influence tipping behavior.
Filter the data from the sidebar to discover dynamic trends and insights.
""")

# Sidebar filters
st.sidebar.header("Filters")
gender = st.sidebar.selectbox("Select Gender", options=df['sex'].unique())
day = st.sidebar.multiselect("Select Days", options=df['day'].unique(), default=df['day'].unique())
bill_range = st.sidebar.slider("Total Bill Range", float(df['total_bill'].min()), float(df['total_bill'].max()), (float(df['total_bill'].min()), float(df['total_bill'].max())))

# Filter data
filtered_df = df[(df['sex'] == gender) & (df['day'].isin(day)) & (df['total_bill'].between(*bill_range))]

# Display data table
st.subheader("Filtered Data Table")
st.dataframe(filtered_df)

# Summary statistics
st.subheader("Summary Statistics")
st.metric("Average Tip", f"${filtered_df['tip'].mean():.2f}")
st.metric("Average Total Bill", f"${filtered_df['total_bill'].mean():.2f}")
st.metric("Total Records", len(filtered_df))

# Scatterplot with Seaborn
st.subheader("Total Bill vs Tip (Scatterplot)")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=filtered_df, x="total_bill", y="tip", hue="smoker", ax=ax1)
st.pyplot(fig1)

# Boxplot
st.subheader("Boxplot of Tip by Day")
fig2, ax2 = plt.subplots()
sns.boxplot(data=filtered_df, x="day", y="tip", ax=ax2)
st.pyplot(fig2)

# Correlation heatmap
st.subheader("Correlation Heatmap")
fig3, ax3 = plt.subplots()
corr = filtered_df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)

# Plotly interactive chart
st.subheader("Interactive Plot: Tip vs Total Bill")
fig4 = px.scatter(filtered_df, x='total_bill', y='tip', color='day', hover_data=['sex', 'smoker'])
st.plotly_chart(fig4)

# Optional CSV upload
st.sidebar.markdown("---")
st.sidebar.subheader("Upload Your Own CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    user_df = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data Preview")
    st.write(user_df.head())
