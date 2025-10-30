import streamlit as st
import random

# 🎀 페이지 기본 설정
st.set_page_config(page_title="로또 번호 생성기", page_icon="🎰", layout="centered")

# 🎨 HTML + CSS 꾸미기
st.markdown("""
    <style>
    body {
        background-color: #ffe6f2;
        background-image: url('https://png.pngtree.com/thumb_back/fw800/background/20230426/pngtree-pink-cherry-blossom-falling-background-image_2529090.jpg');
        background-size: cover;
        background-attachment: fixed;
        font-family: "Noto Sans KR", sans-serif;
    }
    .lotto-ball {
        display: inline-block;
        background: radial-gradient(circle at 30% 30%, #fff, #ff80aa);
        color: #333;
        font-weight: bold;
        font-size: 22px;
        width: 50px;
        height: 50px;
        line-height: 50px;
        border-radius: 50%;
        text-align: center;
        margin: 5px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.2);
    }
    .lotto-container {
        background-color: rgba(255, 255, 255, 0.75);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        text-align: center;
    }
    h1 {
        color: #d63384;
        text-shadow: 1px 1px 3px #fff;
    }
    </style>
""", unsafe_allow_html=True)

# 🌸 제목
st.markdown("<h1>🌸 벚꽃 로또 번호 생성기 🎰</h1>", unsafe_allow_html=True)

# 🎮 입력 및 버튼
game_count = st.number_input("생성할 게임 수를 선택하세요 (1~10)", min_value=1, max_value=10, value=1, step=1)
if st.button("🍀 번호 생성하기"):
    st.markdown('<div class="lotto-container">', unsafe_allow_html=True)
    for i in range(game_count):
        numbers = sorted(random.sample(range(1, 46), 6))
        balls_html = "".join([f"<div class='lotto-ball'>{n}</div>" for n in numbers])
        st.markdown(f"<h3>🎲 {i+1}게임</h3>" + balls_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
