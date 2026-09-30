import streamlit as st
import pandas as pd

st.title("🧹 超強 Excel 智慧資料吸塵器")
st.write("把你的災難級 Excel 丟上來，一秒幫你洗得乾乾淨淨！")

# 上傳檔案元件
uploaded_file = st.file_uploader("上傳你的 Excel 檔案", type=["xlsx", "xls"])

if uploaded_file is not None:
    # 讀取 Excel
    df = pd.read_excel(uploaded_file)
    
    st.subheader("👀 原始資料預覽（災難現場）")
    st.dataframe(df)
    
    # 資料清洗邏輯
    df.columns = df.columns.str.strip() # 去除欄位名稱前後空白
    df = df.dropna(how='all')            # 濾掉全空行
    
    st.subheader("✨ 清洗後的完美表格")
    st.dataframe(df)
    
    # 產生下載按鈕
    output_file = "cleaned_output.xlsx"
    df.to_excel(output_file, index=False)
    
    with open(output_file, "rb") as f:
        st.download_button(
            label="📥 下載處理好的 Excel",
            data=f,
            file_name="clean_output.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )