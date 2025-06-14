import streamlit as st

st.set_page_config(page_title="Ứng dụng tính thuế TNDN", layout="centered")

st.title("📊 Ứng dụng tính thuế cho Doanh Nghiệp Tư Nhân")

# --- Nhập thông tin đầu vào ---
st.header("Nhập thông tin tài chính")
doanh_thu = st.number_input("🔹 Doanh thu trong kỳ (VND)", min_value=0.0, step=1e6, format="%.0f")
chi_phi_duoc_tru = st.number_input("🔹 Chi phí được trừ (VND)", min_value=0.0, step=1e6, format="%.0f")
thue_suat = st.slider("🔹 Thuế suất TNDN (%)", 10.0, 25.0, 20.0)

# --- Tính toán ---
if st.button("📌 Tính thuế"):
    loi_nhuan_truoc_thue = doanh_thu - chi_phi_duoc_tru
    thue_TNDN = loi_nhuan_truoc_thue * (thue_suat / 100)
    loi_nhuan_sau_thue = loi_nhuan_truoc_thue - thue_TNDN

    st.subheader("📈 Kết quả tính thuế")
    st.write(f"✅ Lợi nhuận trước thuế: **{loi_nhuan_truoc_thue:,.0f} VND**")
    st.write(f"💰 Thuế TNDN phải nộp ({thue_suat:.0f}%): **{thue_TNDN:,.0f} VND**")
    st.write(f"💸 Lợi nhuận sau thuế: **{loi_nhuan_sau_thue:,.0f} VND**")

    # Cảnh báo nếu âm
    if loi_nhuan_truoc_thue < 0:
        st.warning("⚠️ Doanh nghiệp đang lỗ nên không phải nộp thuế TNDN.")
