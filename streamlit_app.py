import streamlit as st

st.text("안녕하세요. 반갑습니다.")

st.title("두 개의 버튼 예제")

st.text_input("메시지를 입력하세요:")

if st.button("버튼 1"):
    st.write("첫 번째 버튼이 클릭되었습니다!")

if st.button("버튼 2"):
    st.write("두 번째 버튼이 클릭되었습니다!")

if st.button("버튼 3"):
  st.write("두 번째 버튼이 클릭되었습니다!")
