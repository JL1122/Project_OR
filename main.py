# import time
import streamlit as st
import numpy as np
import pandas as pd

#標題
st.title('手術室器械位置圖')

# 資料對應字典
options = {
    "心臟外科": ["鎖骨下動脈及肺動脈之分流術", "冠狀動脈分流手術", "結紮法"],
    "外 科": ["空腸造口術", "剖腹術", "腹腔鏡膽囊切除術"],
    "泌 尿 科": ["割裂為二", "膀胱頸懸吊術", "探條擴張術"],
    "骨 科":["膝上截肢術","前十字韌帶修補術","壓迫性骨釘"],
    "耳 鼻 喉 科 ":["增殖腺切除術","氣管鏡檢查","閉合性復位"]
}

# 第一個下拉選單: 選擇類別
selected_category = st.sidebar.selectbox("選擇科別", list(options.keys()))

# 第二個下拉選單: 顯示相對應選項
if selected_category:
    selected_item = st.sidebar.selectbox("術 式", options[selected_category])

    
st.write(f"#### 術式: {selected_item}")
