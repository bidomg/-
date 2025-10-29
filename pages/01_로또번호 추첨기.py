import streamlit as st
import random

st.set_page_config(page_title="로또 번호 추첨기", page_icon="🎰", layout="centered")

st.title("🎰 대한민국 로또 번호 추첨기")
st.write("1부터 45까지 숫자 중 6개를 무작위로 추천해드립니다!")

# 세트 수 선택
num_sets = st.slider("몇 세트를 생성할까요?", 1, 10, 3)

# 최근 로또 당첨번호 입력
recent_winning = st.text_input(
    "최근 로또 당첨번호를 입력해주세요 (예: 1, 7, 15, 23, 34, 41)"
)

# 번호 생성 버튼
if st.button("🎲 번호 생성하기"):
    st.subheader("추천된 로또 번호 🎟️")

    # 최근 당첨 번호 파싱
    winning_nums = []
    if recent_winning:
        try:
            winning_nums = [int(x.strip()) for x in recent_winning.split(",") if x.strip()]
        except ValueError:
            st.error("⚠️ 숫자 형식이 올바르지 않습니다. 예: 1, 7, 15, 23, 34, 41")
            winning_nums = []

    for i in range(num_sets):
        lotto_numbers = sorted(random.sample(range(1, 46), 6))
        match_count = len(set(lotto_numbers) & set(winning_nums))

        # 카드 형식 출력
        with st.container():
            st.markdown(f"### 🎯 세트 {i+1}")
            st.markdown(
                f"<h3 style='text-align:center; color:#2E86C1;'>{', '.join(map(str, lotto_numbers))}</h3>",
                unsafe_allow_html=True,
            )

            if winning_nums:
                st.write(f"🔍 최근 당첨번호와 일치한 개수: **{match_count}개**")

                if match_count == 6:
                    st.success("🥇 축하합니다! 1등 가능성이 있습니다!")
                elif match_count >= 4:
                    st.info("🎉 꽤 비슷하네요!")
                elif match_count >= 2:
                    st.warning("😊 일부 번호가 일치합니다.")
                else:
                    st.write("😅 아쉽게도 일치하는 번호가 없습니다.")
        st.divider()

st.caption("💡 행운을 빕니다! (실제 당첨을 보장하지 않습니다.)")
