import streamlit as st
import pandas as pd
from io import StringIO
from PIL import Image
import tempfile
import io
# import cv2 as cv
# x = st.slider("Select a value")
# st.write(x, "squared is", x * x)

st.title('Video Object Detection')

title = st.text_input('Enter things that need to be detected', '')
st.write(title)

# Set page title
st.set_page_config(page_title="Video Player")

# Define a function to read and display videos
def read_video(video_file):
    with open(video_file, 'rb') as f:
        video_bytes = f.read()
    st.video(video_bytes)

# Create a file uploader for videos
video_file = st.file_uploader("Upload a video", type=["mp4", "avi"])

# Display the uploaded video
if video_file is not None:
    read_video(video_file)




             
             



    



