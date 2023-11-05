                                                    #DAY 19
#impliment over ps76.py to overcome Attribute error

import streamlit as st
from PIL import Image

camera_img = st.camera_input("Camera")
if camera_img :
    img = Image.open(camera_img)
    gray_img = img.convert("L")
    st.image(gray_img)

'''
    >>> camera_img = "Hello"
    >>> camera_img2 = None
    >>> if camera_img :
            print("Hai")
    Hai
    
    >>> if camera_img2 :
            print("Yes")
    
    >>>
                                '''