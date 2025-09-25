import streamlit as st

st.title("데이터 예시 페이지")

st.write("이곳은 data.py에서 만든 새로운 페이지입니다.")

# 예시 데이터 테이블
import pandas as pd
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
})
st.dataframe(data)

st.write("원하는 데이터 시각화나 기능을 추가할 수 있습니다.")
