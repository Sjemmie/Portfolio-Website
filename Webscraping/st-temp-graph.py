import streamlit as st
import plotly.express as px

# Set webpage title
st.title("Temperatures webscrape example")

# Set variables
userdata_x = []
userdata_y = []


# Read content for graph
with open("temps.txt", "r") as file:
    content = file.readlines()[1:]
    empty_list = []
for item in content:
    item = item.strip().split(", ")
    userdata_x.append(item[0])
    userdata_y.append(item[1])

figure = px.line(x=userdata_x, y=userdata_y, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)
