import streamlit as st
import numpy as np
import pandas as pd

# 🌸 페이지 설정
st.set_page_config(page_title="유리함수의 개념과 성질", page_icon="🌸", layout="wide")

# 🌸 CSS 테마
st.markdown("""
<style>
    body {
        background-color: #fff5f8;
    }
    .stApp {
        background: linear-gradient(180deg, #ffe6f0 0%, #fff 80%);
        color: #333;
        font-family: 'Apple SD Gothic Neo', sans-serif;
    }
    h1, h2, h3 {
        color: #ff66a3;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffe6f0;
        color: #333;
        border-radius: 10px;
        margin-right: 4px;
        padding: 6px 14px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# 🌸 제목
st.title("🌸 유리함수의 개념과 성질 교과서 🌸")
st.write("아래 단계를 하나씩 눌러보며 유리함수를 배워봐요!")

# 탭 구성
tabs = st.tabs(["1️⃣ 개념 이해", "2️⃣ 그래프 탐구", "3️⃣ 성질 정리", "4️⃣ 문제로 확인하기"])

# 1️⃣ 개념 이해
with tabs[0]:
    st.header("🔹 다항함수와 유리함수의 구분")
    st.markdown("""
    **다항함수 (Polynomial Function)**  
    - x가 분모에 없는 함수  
    - 예: \\( f(x) = 2x^2 + 3x - 1 \\)

    **유리함수 (Rational Function)**  
    - 다항함수의 **비(分)** 로 이루어진 함수  
    - 예: \\( f(x) = \\frac{p(x)}{q(x)}, \\quad q(x) \\neq 0 \\)  
      → \\( f(x) = \\frac{1}{x},\\  \\frac{x+2}{x-1} \\)

    💡 **핵심 차이점:** 분모에 x가 있으면 ‘유리함수’!
    """)

# 2️⃣ 그래프 탐구
with tabs[1]:
    st.header("🔹 유리함수의 기본형과 그래프 변화")

    st.markdown("""
    유리함수의 기본형은  
    \\[
    f(x) = \\frac{1}{x}
    \\]
    입니다.
    """)

    x = np.linspace(-10, 10, 400)
    x = x[x != 0]
    df = pd.DataFrame({"x": x, "y": 1/x})
    st.line_chart(df, x="x", y="y", height=400)

    st.markdown("""
    📍 **y=1/x** → 1, 3사분면  
    📍 **y=-1/x** → 2, 4사분면  
    """)

    st.subheader("⚙️ 그래프 조절해보기")
    a = st.slider("a (기울기/방향)", -3.0, 3.0, 1.0, step=0.5)
    p = st.slider("p (x축 이동)", -5.0, 5.0, 0.0, step=0.5)
    q = st.slider("q (y축 이동)", -5.0, 5.0, 0.0, step=0.5)
    abs_mode = st.checkbox("절댓값 |x| 적용 (y = 1/|x|)")

    x2 = np.linspace(-10, 10, 400)
    x2 = x2[x2 != p]
    if abs_mode:
        y2 = a / np.abs(x2 - p) + q
    else:
        y2 = a / (x2 - p) + q
    df2 = pd.DataFrame({"x": x2, "y": y2})
    st.line_chart(df2, x="x", y="y", height=400)

    st.markdown("""
    🔸 **평행이동**  
    - `p`: x축 방향 이동  
    - `q`: y축 방향 이동  

    🔸 **절댓값 |x| 적용 시**  
    - y축 대칭 형태로 그래프 변화!
    """)

# 3️⃣ 성질 정리
with tabs[2]:
    st.header("🔹 유리함수의 주요 성질 정리")
    st.markdown("""
    | 구분 | 내용 |
    |------|------|
    | **정의역** | 분모가 0이 되는 x 제외 |
    | **점근선** | 분모가 0이 되는 x=p, 수평 점근선 y=q |
    | **대칭성** | y=1/x 는 원점 대칭 |
    | **절댓값 적용 시** | y축 대칭 형태로 변함 |

    💡 **그래프의 기본형 `y = 1/x` 는 원점을 기준으로 좌우 대칭이에요.**
    """)

# 4️⃣ 문제로 확인하기
with tabs[3]:
    st.header("🧩 더 알아보기 - 개념 확인 문제")
    st.write("객관식 문제를 풀면서 개념을 정리해봐요!")

    questions = [
        {"q": "1. 다음 중 유리함수가 아닌 것은?", 
         "choices": ["① y=1/x", "② y=(x+1)/(x-2)", "③ y=x²+1", "④ y=2/x", "⑤ y=(x²+1)/x"], "answer": "③ y=x²+1"},
        {"q": "2. y=1/x 그래프는 어느 사분면에 있을까?", 
         "choices": ["① 1,3사분면", "② 2,4사분면", "③ 1,2사분면", "④ 3,4사분면", "⑤ 모든 사분면"], "answer": "① 1,3사분면"},
        {"q": "3. y=-1/x 그래프는 어느 사분면에 있을까?", 
         "choices": ["① 1,3사분면", "② 2,4사분면", "③ 1,2사분면", "④ 3,4사분면", "⑤ 없음"], "answer": "② 2,4사분면"},
        {"q": "4. y=1/(x-2)+3 의 점근선은?", 
         "choices": ["① x=0,y=0", "② x=2,y=3", "③ x=-2,y=3", "④ x=3,y=2", "⑤ x=3,y=-2"], "answer": "② x=2,y=3"},
        {"q": "5. y=a/x 에서 a<0 일 때, 그래프는?", 
         "choices": ["① 1,3사분면", "② 2,4사분면", "③ x축 대칭", "④ y축 대칭", "⑤ 원점 통과"], "answer": "② 2,4사분면"},
        {"q": "6. 절댓값이 포함된 y=1/|x| 의 그래프는?", 
         "choices": ["① 1,2사분면", "② 2,4사분면", "③ 1,3사분면", "④ 3,4사분면", "⑤ 없음"], "answer": "① 1,2사분면"},
        {"q": "7. 유리함수의 점근선은 평행이동 후 어떻게 변하나?", 
         "choices": ["① 변하지 않는다", "② x=p, y=q 로 이동", "③ x축만 이동", "④ y축만 이동", "⑤ 대칭만 변함"], "answer": "② x=p, y=q 로 이동"}
    ]

    for i, q in enumerate(questions):
        st.markdown(f"**{q['q']}**")
        ans = st.radio("보기", q["choices"], key=f"quiz_{i}")
        if st.button(f"정답 확인 ({i+1}번)"):
            if ans == q["answer"]:
                st.success("🎉 정답입니다!")
            else:
                st.error(f"❌ 오답입니다. 정답은 {q['answer']} 입니다.")

    st.markdown("---")
    st.markdown("<h2 style='text-align:center; color:#ff66a3;'>💖 고생하셨습니다~ 사랑해요 💖</h2>", unsafe_allow_html=True)
