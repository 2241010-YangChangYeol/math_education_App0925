import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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
        st.success("정답입니다! 아래 풀이를 확인하고 다음 문제로 진행하세요.")

        # --- 그래프 생성 ---
        fig, ax = plt.subplots()
        x = np.linspace(-0.5, 3.5, 400)
        y = x**2 - 1
        
        ax.plot(x, y, label='$y=x^2-1$')
        ax.axhline(0, color='black', linewidth=0.5)
        
        # 넓이 영역 채우기
        x_fill_1 = np.linspace(0, 1, 100)
        ax.fill_between(x_fill_1, x_fill_1**2 - 1, 0, color='skyblue', alpha=0.5, label='Area (0≤x≤1)')
        
        x_fill_2 = np.linspace(1, 3, 200)
        ax.fill_between(x_fill_2, x_fill_2**2 - 1, 0, color='lightgreen', alpha=0.5, label='Area (1≤x≤3)')
        
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Graph of $y=x^2-1$ and Area")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

        # --- 풀이 과정 ---
        st.subheader("풀이 과정")
        st.markdown(r"""
        곡선과 $x$축으로 둘러싸인 부분의 넓이를 구하기 위해서는 함수값의 부호를 고려해야 합니다. 즉, 정적분 $\int_0^3 |x^2-1|\,dx$ 값을 계산해야 합니다.

        1.  **피적분 함수의 부호 확인**:
            함수 $y=x^2-1$은 $x=1$에서 $x$축과 만납니다.
            -   구간 $[0, 1]$에서 $x^2-1 \le 0$
            -   구간 $[1, 3]$에서 $x^2-1 \ge 0$

        2.  **구간을 나누어 정적분 계산**:
            따라서, 구간을 $[0, 1]$과 $[1, 3]$으로 나누어 계산해야 합니다.
            $$
            S = \int_0^3 |x^2-1|\,dx = \int_0^1 -(x^2-1)\,dx + \int_1^3 (x^2-1)\,dx
            $$

        3.  **각 구간의 정적분 값 계산**:
            $$
            \begin{aligned}
            \int_0^1 (1-x^2)\,dx &= \left[x - \frac{x^3}{3}\right]_0^1 = \left(1 - \frac{1}{3}\right) - 0 = \frac{2}{3} \\
            \int_1^3 (x^2-1)\,dx &= \left[\frac{x^3}{3} - x\right]_1^3 = \left(\frac{27}{3} - 3\right) - \left(\frac{1}{3} - 1\right) = (9-3) - \left(-\frac{2}{3}\right) = 6 + \frac{2}{3} = \frac{20}{3}
            \end{aligned}
            $$

        4.  **총 넓이 계산**:
            $$
            S = \frac{2}{3} + \frac{20}{3} = \frac{22}{3}
            $$
        따라서, 구하는 넓이는 $\frac{22}{3}$ 입니다.
        """)

        # "다음 문제로 이동" 버튼을 오른쪽에 배치
        _, col2 = st.columns([0.8, 0.2])
        with col2:
            if st.button("다음 문제로 이동", key="next_q2"):
                st.session_state.current_question = 2
                st.rerun()
        return

    # 정답 폼
    with st.form(key='q1_form'):
        options = ["6", "20/3", "22/3", "8"]
        user_answer = st.radio("정답을 선택하세요:", options)
        submitted = st.form_submit_button("답안 제출")

    if submitted:
        st.session_state.q1_answered = True
        if user_answer == "22/3":
            st.session_state.q1_correct = True
            st.rerun()
        else:
            st.session_state.q1_correct = False

    if st.session_state.q1_answered and not st.session_state.q1_correct:
        st.error("오답입니다. 다시 풀어보세요.")
    
    st.markdown("---")

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
