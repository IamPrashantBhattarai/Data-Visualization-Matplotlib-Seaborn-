import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("tips")

# Title and description
st.title("Interactive Tips Dashboard")
st.write("Explore how gender, day, and total bill influence tipping behavior.")

# Sidebar filters
gender = st.sidebar.selectbox("Select Gender", df['sex'].unique())
day = st.sidebar.multiselect("Select Days", df['day'].unique(), default=df['day'].unique())

# Filter data
filtered_df = df[(df['sex'] == gender) & (df['day'].isin(day))]

# Show filtered data
st.dataframe(filtered_df)

# Plot
st.subheader("Total Bill vs Tip")
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_df, x="total_bill", y="tip", hue="smoker", ax=ax)
st.pyplot(fig)
