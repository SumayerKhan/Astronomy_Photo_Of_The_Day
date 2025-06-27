import requests
import streamlit as st

# API
api_key = "a0OPdteZmUhcFEJ2qsQdPRUclZhwPd5ItF9gjYK1"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Fetching the data from API
response = requests.get(url)
content = response.json()

title = content["title"]
description = content["explanation"]
image_url = content["hdurl"]

# Showing in the streamlit
st.title("Astronomy Photo of the Day")
st.header(title)
st.image(image_url)
st.write(description)

