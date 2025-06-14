import streamlit as st
import pandas as pd

st.set_page_config(page_title="📦 Quản lý nguồn hàng điện thoại", layout="wide")

st.title("📱 Ứng dụng Kiểm Tra Nguồn Hàng Sản Phẩm Điện Thoại Trong Kho")

# Upload file CSV
uploaded_file = st.file_uploader("📤 Tải danh sách hàng hóa (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.success("✅ Dữ liệu đã được tải lên!")

    # Bộ lọc tìm kiếm
    with st.expander("🔎 Bộ lọc tìm kiếm nâng cao", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            keyword = st.text_input("🔍 Tìm theo mã, tên sản phẩm hoặc IMEI")
        with col2:
            nha_cc = st.selectbox("🏪 Chọn nhà cung cấp", ["Tất cả"] + df['nhà_cung_cấp'].dropna().unique().tolist())
        with col3:
            tinh_trang = st.multiselect("🔧 Tình trạng sản phẩm", df['tình_trạng'].dropna().unique().tolist(), default=df['tình_trạng'].unique().tolist())

        filtered_df = df.copy()
        if keyword:
            keyword = keyword.lower()
            filtered_df = filtered_df[
                filtered_df.apply(lambda row: keyword in str(row).lower(), axis=1)
            ]
        if nha_cc != "Tất cả":
            filtered_df = filtered_df[filtered_df['nhà_cung_cấp'] == nha_cc]
        if tinh_trang:
            filtered_df = filtered_df[filtered_df['tình_trạng'].isin(tinh_trang)]

    # Hiển thị bảng dữ liệu
    st.subheader("📋 Danh sách sản phẩm")
    st.dataframe(filtered_df, use_container_width=True)

    # Cảnh báo tồn kho thấp
    low_stock = filtered_df[filtered_df['số_lượng'] <= 2]
    if not low_stock.empty:
        st.warning(f"⚠️ Có {len(low_stock)} sản phẩm tồn kho thấp (≤ 2 chiếc)")

    # Thống kê nhanh
    st.subheader("📊 Tổng quan tồn kho")
    total_quantity = filtered_df['số_lượng'].sum()
    total_value = (filtered_df['số_lượng'] * filtered_df['giá_nhập']).sum()
    col1, col2 = st.columns(2)
    col1.metric("📦 Tổng số lượng còn lại", f"{total_quantity:,} chiếc")
    col2.metric("💰 Tổng giá trị tồn kho", f"{total_value:,.0f} VND")

    # Xuất dữ liệu
    csv_download = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Tải báo cáo CSV", data=csv_download, file_name="bao_cao_kho.csv", mime='text/csv')
