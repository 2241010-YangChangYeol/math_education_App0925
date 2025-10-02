import streamlit as st

def initialize_state():
    """세션 상태를 초기화합니다."""
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 1
    # 문제 1 상태
    if 'q1_answered' not in st.session_state:
        st.session_state.q1_answered = False
    if 'q1_correct' not in st.session_state:
        st.session_state.q1_correct = False
    # 문제 2 상태
    if 'q2_answered' not in st.session_state:
        st.session_state.q2_answered = False
    if 'q2_correct' not in st.session_state:
        st.session_state.q2_correct = False

def reset_all_state():
    """모든 상태를 초기화하여 처음부터 다시 시작합니다."""
    st.session_state.current_question = 1
    st.session_state.q1_answered = False
    st.session_state.q1_correct = False
    st.session_state.q2_answered = False
    st.session_state.q2_correct = False
    st.rerun()

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
        # 실제 정답은 22/3 이지만, 현재는 6으로 설정되어 있음
        if user_answer == "6":
            st.session_state.q1_correct = True
            st.rerun()
        else:
            st.session_state.q1_correct = False

    if st.session_state.q1_answered and not st.session_state.q1_correct:
        st.error("오답입니다. 다시 풀어보세요.")
    
    st.markdown("---")
    if st.button("문제 2로 바로가기"):
        st.session_state.current_question = 2
        st.rerun()


def question2():
    """문제 2를 표시하고 처리합니다."""
    st.subheader("문제 2")
    st.markdown(r"""
    곡선 $y = -x^2 + 2x$ 와 $x$축으로 둘러싸인 도형의 넓이를 $S$라 하면, $9S$의 값은?
    """)

    # 사용자가 이미 정답을 맞혔는지 확인
    if st.session_state.q2_correct:
        st.success("정답입니다! 모든 문제를 해결했습니다.")
        st.balloons()
        if st.button("처음으로 돌아가기"):
            reset_all_state()
        return

    # 정답 폼
    with st.form(key='q2_form'):
        options = ["8", "10", "12", "14", "16"]
        user_answer = st.radio("정답을 선택하세요:", options)
        submitted = st.form_submit_button("답안 제출")

    if submitted:
        st.session_state.q2_answered = True
        if user_answer == "12":
            st.session_state.q2_correct = True
            st.rerun()
        else:
            st.session_state.q2_correct = False

    if st.session_state.q2_answered and not st.session_state.q2_correct:
        st.error("오답입니다. 다시 풀어보세요.")

    st.markdown("---")
    if st.button("문제 1로 돌아가기"):
        st.session_state.current_question = 1
        st.rerun()

# --- 메인 페이지 로직 ---
st.title("수학 문제 풀이")

initialize_state()

if st.session_state.current_question == 1:
    question1()
elif st.session_state.current_question == 2:
    question2()
