import streamlit as st
# x = st.slider("Select a value")
# st.write(x, "squared is", x * x)

st.title('Video Object Detection')

title = st.text_input('Enter things that need to be detected', '')
st.write('The current movie title is', title)

