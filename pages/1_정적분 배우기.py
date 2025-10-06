import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from pathlib import Path

# 한글 폰트 설정
font_path = str(Path(__file__).parent.parent / 'fonts' / 'NanumGothic-Regular.ttf')
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())
plt.rcParams['axes.unicode_minus'] = False

st.title("적분의 직사각형 근사와 넓이 계산")

st.write(r"""
#### 수학에서의 정적분 정의
닫힌구간 $[a, b]$에서 연속이고 $f(x) \ge 0$인 함수 $f(x)$에 대해, 함수 $f(x)$의 그래프와 $x$축으로 둘러싸인 도형의 넓이를 $f(x)$의 $a$에서 $b$까지의 **정적분**이라 한다.
""")

st.write(r"""
### 정의: 정적분
수학에서 정적분은 함수 그래프 아래 영역의 넓이를 나타내며, 다음과 같이 표현됩니다.
$$
\int_a^b f(x)\,dx
$$
""")

st.write("""
### 개념: 리만 합 (Riemann Sum)
곡선으로 둘러싸인 영역의 넓이를 직접 계산하는 것은 복잡할 수 있습니다. 그래서 간단한 도형인 **직사각형**을 사용하여 넓이를 근사하는 방법을 사용합니다.

이것을 **리만 합**이라고 부릅니다. 영역을 여러 개의 얇은 직사각형으로 나누고, 그 직사각형들의 넓이를 모두 더하여 전체 넓이를 추정하는 원리입니다. 직사각형의 개수를 늘릴수록 실제 넓이에 더 가까워집니다.

아래는 함수 $f(x) = x^2$의 그래프와, 그 아래 영역을 10개의 직사각형으로 근사한 예시입니다.
""")

# --- 직사각형 개수 슬라이더 추가 ---
n = st.slider('직사각형 개수 n', min_value=2, max_value=100, value=10)

# 예시: f(x) = x^2, [0, 2] 구간
f = lambda x: x**2
a, b = 0, 2

# 그래프를 위한 x, y 값
x_curve = np.linspace(a, b, 500)
y_curve = f(x_curve)

# 직사각형 계산을 위한 값
x_rect = np.linspace(a, b, n + 1)
x_mid = (x_rect[:-1] + x_rect[1:]) / 2
dx = (b - a) / n
y_rect = f(x_mid)

# 근사 넓이 계산
total_area = np.sum(y_rect * dx)

# 그래프 생성
fig, ax = plt.subplots()

# 직사각형 막대 그래프
ax.bar(x_mid, y_rect, width=dx, alpha=0.5, color='orange', edgecolor='black', label=f'{n}')

# 함수 곡선
ax.plot(x_curve, y_curve, color='blue', linewidth=2, label='$f(x) = x^2$')

ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
st.pyplot(fig)

st.write(f"**계산된 근사 넓이 (직사각형 {n}개):** `{total_area:.4f}`")

st.info("직사각형의 개수(n)를 늘릴수록 실제 적분 값에 더 가까워집니다.")
