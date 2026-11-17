import streamlit as st

with st.form('my_form'):
    name = st.text_input('이름')
    age = st.number_input('나이', min_value=0, value=10, step=1)
    agreed = st.checkbox('약관에 동의합니다.')
    submitted = st.form_submit_button('제출')

if submitted:
    st.info(f'이름 : {name}, 나이 : {age}')
    if agreed:
        st.info('약관 동의함')

import time
@st.cache_data
def change_text():
    text = st.title('메가몬 진화 ~')
    time.sleep(5)
    text.info('진화 성공 !!')

change_text()

