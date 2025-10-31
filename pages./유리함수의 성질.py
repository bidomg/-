import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 🌟 기본 설정
st.set_page_config(page_title="유리함수의 개념과 성질", page_icon="📘", layout="wide")

# 🎓 제목
st.title("📘 유리함수의 개념과 성질 학습 페이지")

st.markdown("""
---
## 🔹 1. 다항함수와 유리함수의 구분
**다항함수(polynomial function)** 는 변수 `x`가 **분모에 없는 함수**로, 예를 들어  
\\( f(x) = 2x^2 + 3x - 1 \\) 과 같은 형태입니다.  

반면 **유리함수(rational function)** 는 다항함수의 **비(分)** 로 이루어진 함수예요.  
즉,  
\\[
f(x) = \\frac{p(x)}{q(x)} \\quad (단,\\ q(x) \\neq 0)
\\]
형태로, 분모에 `x`가 들어가면 유리함수입니다.  
대표적인 예로  
\\( f(x) = \\frac{1}{x} \\) 또는 \\( f(x) = \\frac{x+2}{x-1} \\) 등이 있어요.
---
""")

# 📊 2. 그래프 시각화 (y = 1/x 기본형)
st.header("🔹 2. 유리함수의 기본형 그래프와 사분면 구분")

x = np.linspace(-10, 10, 400)
x = x[x != 0]  # 0으로 나누는 것 방지
y = 1/x

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, color="hotpink", linewidth=2)
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(0, color='gray', linewidth=0.8)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_title("y = 1/x 의 그래프 (기본형)")
ax.grid(True, linestyle="--", alpha=0.5)
st.pyplot(fig)

st.markdown("""
유리함수의 대표적인 기본형인 **y = 1/x** 는  
1사분면과 3사분면에 그래프가 나타나요.  
그 이유는,  
- x가 양수 → y도 양수 (1사분면)  
- x가 음수 → y도 음수 (3사분면)  
이기 때문이에요.  

반면 **y = -1/x** 는 부호가 반대이므로 2사분면과 4사분면에 그래프가 나타나죠.
---
""")

# ⚙️ 3. 평행이동과 절댓값 변화 시각화
st.header("🔹 3. 평행이동과 절댓값에 따른 변화")

st.write("아래 슬라이더로 `a`, `p`, `q` 값을 바꿔보세요 👇")

a = st.slider("a (그래프의 모양과 방향)", -3.0, 3.0, 1.0, step=0.5)
p = st.slider("p (x축 방향 이동)", -5.0, 5.0, 0.0, step=0.5)
q = st.slider("q (y축 방향 이동)", -5.0, 5.0, 0.0, step=0.5)
abs_mode = st.checkbox("절댓값 |x| 적용 (y = 1/|x| 형태)")

x = np.linspace(-10, 10, 400)
x = x[x != p]  # 분모 0 방지
if abs_mode:
    y = a / np.abs(x - p) + q
else:
    y = a / (x - p) + q

fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.plot(x, y, color="deepskyblue", linewidth=2)
ax2.axhline(0, color='gray', linewidth=0.8)
ax2.axvline(0, color='gray', linewidth=0.8)
ax2.grid(True, linestyle="--", alpha=0.5)
ax2.set_xlim(-10, 10)
ax2.set_ylim(-10, 10)
ax2.set_title(f"y = {a}/(x - {p}) + {q}")
st.pyplot(fig2)

st.markdown("""
**👉 변화 요약**
- `p` 값은 **x축 방향 평행이동**  
- `q` 값은 **y축 방향 평행이동**  
- `a` 값은 그래프의 **방향과 크기**를 결정  
- 절댓값을 적용하면 **좌우 대칭 형태**가 만들어집니다.
---
""")

# 🧠 4. 기타 개념 추가
st.header("🔹 4. 유리함수의 특징 정리")

st.markdown("""
| 구분 | 내용 |
|------|------|
| **정의역** | 분모가 0이 되는 x는 제외 |
| **비연속점(점근선)** | 분모가 0이 되는 직선 (예: x = 0) |
| **대칭성** | y = 1/x 는 원점 대칭 |
| **평행이동 후 점근선** | x = p, y = q 가 점근선이 됨 |
| **절댓값 포함 시** | 그래프가 y축 기준으로 대칭 |
---
""")

# 🧩 5. 더 알아보기 (문제)
st.header("🧩 더 알아보기 - 개념 확인 문제")

questions = [
    {
        "q": "1. 다음 중 유리함수가 아닌 것은?",
        "choices": ["① y = 1/x", "② y = x/3", "③ y = 2x + 1", "④ y = (x+1)/(x-2)", "⑤ y = (x²+1)/(x)"],
        "answer": "③ y = 2x + 1"
    },
    {
        "q": "2. y = 1/x 그래프는 어떤 사분면에 나타날까?",
        "choices": ["① 1,2사분면", "② 2,4사분면", "③ 1,3사분면", "④ 3,4사분면", "⑤ 모든 사분면"],
        "answer": "③ 1,3사분면"
    },
    {
        "q": "3. y = -1/x 의 그래프는?",
        "choices": ["① 1,3사분면", "② 2,4사분면", "③ 1,2사분면", "④ 3,4사분면", "⑤ 2사분면만"],
        "answer": "② 2,4사분면"
    },
    {
        "q": "4. y = 1/(x-2) + 3 의 점근선은?",
        "choices": ["① x=0, y=0", "② x=2, y=3", "③ x=-2, y=3", "④ x=3, y=2", "⑤ x=-3, y=-2"],
        "answer": "② x=2, y=3"
    },
    {
        "q": "5. y = a/x 에서 a가 음수일 때, 그래프는?",
        "choices": ["① 1,3사분면", "② 2,4사분면", "③ y축 대칭", "④ x축 위", "⑤ 원점 통과"],
        "answer": "② 2,4사분면"
    },
    {
        "q": "6. 절댓값이 있는 y = 1/|x| 의 그래프는?",
        "choices": ["① 1,3사분면", "② 2,4사분면", "③ 1,2사분면", "④ 3,4사분면", "⑤ 원점만 통과"],
        "answer": "③ 1,2사분면"
    },
    {
        "q": "7. 유리함수의 그래프가 평행이동되었을 때 점근선이 변하는 방향은?",
        "choices": ["① 항상 x축 방향", "② 항상 y축 방향", "③ p와 q 방향 모두", "④ 변하지 않는다", "⑤ 대칭 이동만 한다"],
        "answer": "③ p와 q 방향 모두"
    },
]

for i, q in enumerate(questions):
    st.markdown(f"**{q['q']}**")
    answer = st.radio("보기", q["choices"], key=f"quiz_{i}")
    if st.button(f"정답 확인 ({i+1}번)"):
        if answer == q["answer"]:
            st.success("🎉 정답입니다!")
        else:
            st.error(f"❌ 오답입니다. 정답은 {q['answer']} 입니다.")

st.markdown("""
---
# 💖 고생하셨습니다~ 사랑해요 💖
""")
