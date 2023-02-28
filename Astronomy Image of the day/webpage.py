import requests
import streamlit as st


api = "BZcF9BoQu00bxkJNMeZQuwArf4S7phuUOMGpiLCV"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api}"

# get data from website
response = requests.get(url)
content = response.json()

# set dynamic picture for the website
image_url = content["hdurl"]
response_pic = requests.get(f"{image_url}")
content_pic = response_pic.content
with open("image.jpg", "wb") as file:
    file.write(response_pic.content)

# set dynamic parameters
text = content["explanation"]
title = content["title"]
image = "image.jpg"


# make streamlit website
st.title("NASA picture of the Day")
st.subheader(title)
st.image(image)
st.write(text)