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
# 로그함수 밑 입력창 추가
log_base = None
import re
if re.match(r"log\s*\(.*\)", func_str):
    log_base = st.text_input("로그함수의 밑을 입력하세요 (예: 2)", value="")

# x값 입력 UI (함수에 x가 포함된 경우)


a = st.number_input("적분 시작값 a", value=0.0)
b = st.number_input("적분 끝값 b", value=1.0)

if st.button("적분 그래프 그리기"):
    x = Symbol('x')
    try:
        func_expr = func_str.replace('^', '**')
        # 분수표현: a/b, a/(x+1), (x+1)/2 등 다양한 케이스를 괄호로 감싸서 sympy가 안전하게 해석하도록 변환
        # 1) 숫자/식, 2) 식/식, 3) 식/숫자 모두 지원
        # 괄호 없는 a/b -> (a)/(b)로 변환 (단, a, b는 숫자, 문자, 괄호, x 등 모두 가능)
        func_expr = re.sub(r'(?<![\w)])\s*([\w\d\.\+\-\*]+)\s*/\s*([\w\d\.\+\-\*xX\(\)]+)', r'(\1)/(\2)', func_expr)
        # log(x)일 때 밑이 입력되면 log(x, base)로 변환
        if log_base and log_base.strip():
            func_expr = re.sub(r"log\s*\(([^)]+)\)", f"log(\\1, {log_base})", func_expr)
        func = sympify(func_expr)
        f_lamb = lambdify(x, func, 'numpy')
        X = np.linspace(a, b, 400)
        Y = f_lamb(X)
        # Y가 스칼라(상수)일 경우 X와 같은 shape으로 변환
        import numpy as np
        if np.isscalar(Y):
            Y = np.full_like(X, Y)

        # 적분값 계산
        integral_val = integrate(func, (x, a, b)).evalf()

        # 폰트 설정
        try:
            font_path = 'fonts/NanumGothic-Regular.ttf'
            font_name = fm.FontProperties(fname=font_path).get_name()
            plt.rc('font', family=font_name)
            plt.rcParams['axes.unicode_minus'] = False
        except FileNotFoundError:
            st.error(f"폰트 파일을 찾을 수 없습니다: {font_path}. 'fonts' 디렉토리에 폰트 파일이 있는지 확인하세요.")
            # 대체 폰트 사용
            plt.rc('font', family='sans-serif')
            plt.rcParams['axes.unicode_minus'] = False

        fontprop = fm.FontProperties(fname=font_path)
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
