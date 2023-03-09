import streamlit as st
import os
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
from pathlib import Path

# Create analyze instance
analyze = SentimentIntensityAnalyzer()

# Title for webpage
st.title("Diary Tone")
st.subheader("Positivity")

# Get files
dir_path = r"C:\Users\youri\PycharmProjects\Portfolio Website\MoodDashboard"
files = os.listdir(dir_path)

# Add each file to a list
file_list = []
for file in files:
    if file.endswith(".txt"):
        file_list.append(file)

# Get title from each document and set it as date
dates = []
for file in file_list:
    f = Path(file).stem
    dates.append(f)

# List with positive scores
pos_score = []

# List with negative score
neg_score = []

# Add score to positive or negative list
for file in file_list:
    with open(file, "r") as f:
        text = f.read()
        score = analyze.polarity_scores(text)
        pos_score.append(score["pos"])
        neg_score.append(score["neg"])

# Plot positive scores
figure = px.line(x=dates, y=pos_score, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")

# Plot negative scores
figure1 = px.line(x=dates, y=neg_score, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure1)
