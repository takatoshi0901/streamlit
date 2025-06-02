import streamlit as st
import pandas as pd
from PIL import Image

# レイアウトとタイトルの設定
st.set_page_config(layout="centered")
st.title("Streamlit 単体アプリ")

# CSVファイルの処理
st.header("CSVファイル処理（先頭5行の抽出）")
uploaded_csv = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_csv is not None:
    df = pd.read_csv(uploaded_csv)
    st.write("ファイルを処理しました。先頭5行は以下の通りです：")
    st.write(df.head())

# 画像ファイルの処理
st.header("画像ファイル処理（グレースケール）")
uploaded_img = st.file_uploader("画像ファイルをアップロードしてください", type=["png", "jpg", "jpeg"])

if uploaded_img is not None:
    image = Image.open(uploaded_img)
    gray_image = image.convert("L")
    st.write("画像をグレースケールに変換しました。")
    st.image(image)