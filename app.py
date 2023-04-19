import streamlit as st
import cv2
# x = st.slider("Select a value")
# st.write(x, "squared is", x * x)

st.title('Video Object Detection')

title = st.text_input('Enter things that need to be detected', '')
st.write(title)

st.title("Upload and Play Video")
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file)



