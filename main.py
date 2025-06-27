import requests
import streamlit as st

api_key = "a0OPdteZmUhcFEJ2qsQdPRUclZhwPd5ItF9gjYK1"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
content = response.json()

title = content["title"]
description = content["explanation"]
image_url = content["hdurl"]
image_response = requests.get(image_url)


with open("image.jpg", "wb") as photo:
    photo.write(image_response.content)