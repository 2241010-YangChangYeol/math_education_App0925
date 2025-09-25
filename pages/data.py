import streamlit as st
st.write(r"""
적분의 리만 합 공식:

$$
	ext{부피} \approx \sum_{i=1}^{n} f(x_i) \Delta x
$$
""")
import numpy as np
import matplotlib.pyplot as plt

st.title("적분의 직사각형 근사와 부피 계산")

st.write("""
적분은 곡선 아래의 넓이를 구하는 과정입니다. 이 넓이를 구할 때, 구간을 여러 개의 작은 직사각형으로 나누어 근사할 수 있습니다. 이 방법을 리만 합(Riemann Sum)이라고 하며, 각 직사각형의 넓이를 모두 더하면 전체 곡선 아래의 넓이에 가까워집니다.
직사각형의 넓이(=부피)는 다음과 같이 계산합니다:


$$
	ext{부피} \approx \sum_{i=1}^{n} f(x_i) \Delta x
$$

여기서 $f(x_i)$는 각 구간에서의 함수값, $\Delta x$는 직사각형의 너비입니다.
""")

# 예시: f(x) = x^2, [0, 2] 구간, 직사각형 10개
f = lambda x: x**2
a, b = 0, 2
n = 10
X = np.linspace(a, b, n+1)
X_mid = (X[:-1] + X[1:]) / 2
dx = (b - a) / n
Y = f(X_mid)
rect_areas = Y * dx
total_volume = np.sum(rect_areas)

fig, ax = plt.subplots()
ax.bar(X_mid, Y, width=dx, alpha=0.4, color='orange', edgecolor='black', label='직사각형')
ax.plot(np.linspace(a, b, 100), f(np.linspace(a, b, 100)), color='blue', label='f(x)')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.set_title('직사각형 근사와 곡선')
st.pyplot(fig)

st.write(f"직사각형들의 부피(넓이) 합: {total_volume:.4f}")

st.info("직사각형 개수를 늘릴수록 실제 적분값에 가까워집니다.")
