import streamlit as st
import random

# Khởi tạo điểm số nếu chưa có
if 'score' not in st.session_state:
    st.session_state.score = 0

st.set_page_config(page_title="Football Bet Simulator", page_icon="⚽")
st.title("⚽ Football Bet Simulator")

st.markdown("## Barcelona 🆚 Real Madrid")

# Người dùng chọn cược
bet = st.selectbox("Chọn đội bạn đặt cược:", ["Barcelona", "Draw", "Real Madrid"])
if st.button("Đặt Cược"):
    outcome = random.choice(["Barcelona", "Draw", "Real Madrid"])
    
    st.markdown(f"### Kết quả trận đấu: **{outcome}**")

    if bet == outcome:
        st.success("🎉 Bạn đã thắng cược! +10 điểm")
        st.session_state.score += 10
    else:
        st.error("❌ Bạn đã thua cược! -5 điểm")
        st.session_state.score -= 5

st.markdown(f"### ✅ Tổng điểm của bạn: **{st.session_state.score}**")

# Reset điểm
if st.button("Reset điểm"):
    st.session_state.score = 0
    st.info("Điểm đã được reset.")
