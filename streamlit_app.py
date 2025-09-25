
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sympy import sympify, Symbol, lambdify, integrate
st.title("적분 그래프 시각화 앱")



# 함수 입력 및 버튼
st.write("아래 버튼을 클릭하면 함수가 입력란에 추가됩니다.")
default_func = "x^2"
func_examples = {
    "삼각함수": ["sin(x)", "cos(x)", "tan(x)"],
    "로그함수": ["log(x)", "ln(x)"],
    "초월함수": ["exp(x)", "sqrt(x)"]
}

if "func_input" not in st.session_state:
    st.session_state["func_input"] = default_func

col1, col2, col3 = st.columns(3)
for idx, (cat, funcs) in enumerate(func_examples.items()):
    with [col1, col2, col3][idx]:
        for f in funcs:
            if st.button(f"{f}", key=f"btn_{f}"):
                st.session_state["func_input"] = f
                st.rerun()

func_str = st.text_input("함수를 입력하세요 (예: x^2)", value=st.session_state["func_input"], key="func_input")

# x값 입력 UI (함수에 x가 포함된 경우)


a = st.number_input("적분 시작값 a", value=0.0)
b = st.number_input("적분 끝값 b", value=1.0)

if st.button("적분 그래프 그리기"):
    x = Symbol('x')
    try:
        func = sympify(func_str.replace('^', '**'))
        f_lamb = lambdify(x, func, 'numpy')
        X = np.linspace(a, b, 400)
        Y = f_lamb(X)

        # 적분값 계산
        integral_val = integrate(func, (x, a, b)).evalf()

        font_path = "fonts/NanumGothic-Regular.ttf"
        fontprop = fm.FontProperties(fname=font_path)
        plt.rc('font', family=fontprop.get_name())

        fig, ax = plt.subplots()
        ax.plot(X, Y, label=f"f(x) = {func_str}", color='blue')
        ax.fill_between(X, Y, where=[True]*len(X), alpha=0.3, color='orange', label="적분 영역")
        ax.set_xlabel("x", fontproperties=fontprop)
        ax.set_ylabel("f(x)", fontproperties=fontprop)
        ax.legend(prop=fontprop)
        ax.set_title(f"{a}에서 {b}까지의 적분값: {integral_val:.4f}", fontproperties=fontprop)
        ax.axhline(0, color='black', linewidth=1)  # y축(수평선)
        ax.axvline(0, color='black', linewidth=1)  # x축(수직선)
        ax.grid(True, linestyle='--', alpha=0.5)   # 격자선
        st.pyplot(fig)
        st.success(f"적분값: {integral_val:.4f}")

    except Exception as e:
        st.error(f"함수 해석 또는 계산 오류: {e}")
