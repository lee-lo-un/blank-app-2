import streamlit as st

st.title("chat bot - test")
st.text("국영수 중 한 과목을 입력해주세요 ")


input = st.text_input("과목을 입력하세요:")
if st.button("챗봇에게 보내기"):
    # 간단한 응답을 제공하는 챗봇 기능 예제
    if input:
        if "국어" in input:
            response = "Korean"
        elif "영어" in input:
            response = "English"
        elif "수학" in input:
            response = "Math"
        else:
            response = "국영수 과목을 입력해주세요"
        
        st.write("영어 번역: ", response)
    else:
        st.write("국어, 영어 수학 중 한 과목을 입력해주세요")
