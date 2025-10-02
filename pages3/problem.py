import streamlit as st

# 세션 상태 초기화
if 'problem_idx' not in st.session_state:
    st.session_state.problem_idx = 0
if 'show_next_button' not in st.session_state:
    st.session_state.show_next_button = False

# 문제 데이터 정의 (리스트 형태로 여러 문제 추가 가능)
problems = [
    {
        "question": r"""
        함수 $f(x)$가 닫힌구간 $[0, 2]$ 에서 연속일 때,
        
        곡선 $y=f(x)$와 $x$축 및 두 직선 $x=0, x=2$로 둘러싸인 부분의 넓이 $S$를 올바르게 표현한 것은 무엇일까요?
        """,
        "options": {
            r"$f(2) - f(0)$": False,
            r"$\int_0^2 f(x)\,dx$": True,
            r"$f'(2)$": False,
            r"$2 \times f(2)$": False
        }
    },
    {
        "question": "다음 문제의 내용입니다. (여기에 두 번째 문제를 추가할 수 있습니다.)",
        "options": {
            "정답": True,
            "오답1": False,
            "오답2": False
        }
    }
]

st.title(f"수학 문제 풀이 (문제 {st.session_state.problem_idx + 1})")

# 현재 문제 가져오기
current_problem = problems[st.session_state.problem_idx]

st.markdown(current_problem["question"])
st.write("---")

# 정답 제출 후 다음 문제로 넘어갈 수 있을 때
if st.session_state.show_next_button:
    st.success("정답입니다! 다음 문제로 진행하세요.")
    if st.button("다음 문제로", key="next"):
        # 다음 문제로 인덱스 이동
        if st.session_state.problem_idx < len(problems) - 1:
            st.session_state.problem_idx += 1
            st.session_state.show_next_button = False
            st.rerun()
        else:
            st.balloons()
            st.header("모든 문제를 다 푸셨습니다! 축하합니다!")
else:
    # 객관식 선택지
    option_list = list(current_problem["options"].keys())
    user_answer = st.radio("답을 선택하세요:", option_list, key=f"problem_{st.session_state.problem_idx}")

    if st.button("정답 제출", key="submit"):
        # 정답 확인
        if current_problem["options"][user_answer]:
            st.session_state.show_next_button = True
            st.rerun()
        else:
            st.error("오답입니다. 다시 시도해보세요.")
