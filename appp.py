import streamlit as st
from datetime import date as dt_date
from heat_risk import calc_risk

st.set_page_config(page_title="熱中症リスクチェック", page_icon="🌤️", layout="centered")
st.title("熱中症リスクチェックアプリ")
st.caption("入力 → 分析 → 可視化")

# 入力フォーム
with st.form("input"):
    d = st.date_input("日付", value=dt_date.today())
    temp = st.number_input("気温（℃）", min_value=0, max_value=50, value=30, step=1)
    humidity = st.slider("湿度（％）", 0, 100, 60)
    hours = st.number_input("作業時間（時間）", 0.0, 12.0, 1.0)
    submitted = st.form_submit_button("リスクを判定する")

if submitted:
    wbgt, level, comment = calc_risk(temp, humidity, hours)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("WBGT（推定値）", f"{wbgt:.1f}")
        st.subheader(f"リスクレベル：{level}")
    with col2:
        st.progress(min(int(wbgt / 40 * 100), 100))

    st.write(comment)
