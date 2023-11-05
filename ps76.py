                                                                #DAY 19

import streamlit as st
from PIL import Image

#start the camera & streamlit img is created
camera_img = st.camera_input("camera")

#create a pillow image instance
img = Image.open(camera_img)

#convert pillow img to grayscale
gray_img = img.convert("L")

#display the image
st.image(gray_img)