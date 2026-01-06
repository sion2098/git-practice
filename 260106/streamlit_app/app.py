import streamlit as st

st.title("🐳 Docker + Streamlit 실습")
st.write("이 앱은 Docker 컨테이너에서 실행 중입니다!")

# 사용자 입력
name = st.text_input("이름을 입력하세요", "학생")
st.write(f"안녕하세요, **{name}**님!")

# 슬라이더
age = st.slider("나이를 선택하세요", 0, 100, 25)
st.write(f"나이: {age}세")

# 버튼
if st.button("클릭하세요!"):
    st.balloons()
    st.success("�� 축하합니다! Docker 개발 환경 구축 완료!")

# app.py 하단에 추가
st.divider()
st.header("📊 간단한 차트")

import pandas as pd
import numpy as np

# 샘플 데이터 생성
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(chart_data)