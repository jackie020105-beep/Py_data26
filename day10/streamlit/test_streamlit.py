import streamlit as st

st.title("Hello, Streamlit World")

name = "Yujin"
st.title(f"Hello, {name} Welcome to Streamlit World")
st.title("바보멍청이")

import pandas as pd
df = pd.DataFrame({
    'A' : [1,2,3,4,]
    ,'B' : [10, 20, 30, 40]
})
st.write(df)
st.header(name)
st.info(name)
st.error(name)
st.success(name)

import time
text = st.title("나 변한다~!")
time.sleep(5)
text.info("변했당!")