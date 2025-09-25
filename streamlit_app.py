
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sympy import sympify, Symbol, lambdify, integrate

st.title("적분 그래프 시각화 앱")

# 사용자 입력: 함수, 구간
func_str = st.text_input("함수를 입력하세요 (예: x^2)", value="x^2")
a = st.number_input("적분 시작값 a", value=0.0)
b = st.number_input("적분 끝값 b", value=1.0)

if st.button("적분 그래프 그리기"):
    x = Symbol('x')
    try:
        func = sympify(func_str)
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
        st.pyplot(fig)
        st.success(f"적분값: {integral_val:.4f}")
    except Exception as e:
        st.error(f"함수 해석 또는 계산 오류: {e}")
