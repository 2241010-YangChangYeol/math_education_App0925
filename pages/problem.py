import streamlit as st

def initialize_state():
    """세션 상태를 초기화합니다."""
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 1
    if 'q1_answered' not in st.session_state:
        st.session_state.q1_answered = False
    if 'q1_correct' not in st.session_state:
        st.session_state.q1_correct = False

def question1():
    """문제 1을 표시하고 처리합니다."""
    st.subheader("문제 1")
    st.markdown(r"""
    곡선 $y=x^2-1$이 닫힌구간 $[0, 3]$에서 연속일 때, 이 곡선과 $x$축 밑 두 직선 $x=0, x=3$으로 둘러싸인 부분의 넓이는?
    """)

    # 사용자가 이미 정답을 맞혔는지 확인
    if st.session_state.q1_correct:
        st.success("정답입니다! 다음 문제로 진행하세요.")
        if st.button("다음 문제로 이동"):
            st.session_state.current_question = 2
            st.rerun()
        return

    # 정답 폼
    with st.form(key='q1_form'):
        options = ["3", "4", "5", "6", "7"]
        user_answer = st.radio("정답을 선택하세요:", options)
        submitted = st.form_submit_button("답안 제출")

    if submitted:
        st.session_state.q1_answered = True
        if user_answer == "6":
            st.session_state.q1_correct = True
            st.rerun() # 정답 상태를 즉시 반영하기 위해 rerun
        else:
            st.session_state.q1_correct = False

    if st.session_state.q1_answered and not st.session_state.q1_correct:
        st.error("오답입니다. 다시 풀어보세요.")

def question2():
    """문제 2의 플레이스홀더입니다."""
    st.subheader("문제 2")
    st.write("준비 중입니다.")
    if st.button("이전 문제로 돌아가기"):
        st.session_state.current_question = 1
        # 상태 초기화
        st.session_state.q1_answered = False
        st.session_state.q1_correct = False
        st.rerun()

# --- 메인 페이지 로직 ---
st.title("수학 문제 풀이")

initialize_state()

if st.session_state.current_question == 1:
    question1()
elif st.session_state.current_question == 2:
    question2()
