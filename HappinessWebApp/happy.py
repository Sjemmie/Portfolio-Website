import streamlit as st
import pandas as pd
import plotly.express as px

# Set title for the page
st.title("In Search for Happiness")

# Create dataframe
df = pd.read_csv("../HappinessWebApp/happy.csv")
options = df.columns[1:]

# Create selectbox
data_x = st.selectbox(label="Select the data for the X-axis", options=options, key="dataX")
data_y = st.selectbox(label="Select the data for the Y-axis", options=options, key="dataY")

# Get user input to filter data from CSV
userdata_x = df[f"{data_x}"]
userdata_y = df[f"{data_y}"]

figure = px.scatter(x=userdata_x, y=userdata_y, labels={"x": f"{data_x}", "y": f"{data_y}"})
st.plotly_chart(figure)
