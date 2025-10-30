import streamlit as st
import random

st.title("🎰 로또 번호 생성기")

# 게임 수 입력 (1~10)
game_count = st.number_input("몇 게임을 생성하시겠습니까?", min_value=1, max_value=10, step=1, value=1)

if st.button("번호 생성하기"):
    results = []
    for _ in range(game_count):
        numbers = random.sample(range(1, 46), 6)
        numbers.sort()
        results.append(numbers)

    st.subheader("🎯 추천 번호")
    for i, game in enumerate(results, start=1):
        st.write(f"{i}게임: ", ", ".join(map(str, game)))
