import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect('tempdata.db')
cursor = connection.cursor()

# Set webpage title
st.title("Temperatures webscrape example")


# Get variables from SQL database
date = cursor.execute("SELECT date from Temperatus")
date = [item[0] for item in date]

temperature = cursor.execute("SELECT temperature from Temperatus")
temperature = [item[0] for item in temperature]

figure = px.line(x=date, y=temperature, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)
