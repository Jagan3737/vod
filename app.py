import streamlit as st
# x = st.slider("Select a value")
# st.write(x, "squared is", x * x)

st.title('Video Object Detection')

title = st.text_input('Enter things that need to be detected', '')
st.write(title)

import streamlit as st
import pandas as pd
from io import StringIO

file = st.file_uploader("Upload file", type=["csv", "png", "jpg"])
show_file = st.empty()

if not file:
    show_file.info("Please upload a file of type: " + ", ".join(["csv", "png", "jpg"]))

content = file.getvalue()

if isinstance(file, BytesIO):
    show_file.image(file)
else:
    data = pd.read_csv(file)
    st.dataframe(data.head(10))
file.close()
    



