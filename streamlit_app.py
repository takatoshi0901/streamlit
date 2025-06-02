import streamlit as st
import pandas as pd
from PIL import Image

# レイアウトとタイトルの設定
st.set_page_config(layout="centered")
st.title("Streamlit 単体アプリ")

# CSVファイルの処理
st.header("CSVファイル処理（先頭5行の抽出）")
uploaded_csv = st.file_uploader("CSVファイルをアップロードしてね", type=["csv"])

if uploaded_csv is not None:
    df = pd.read_csv(uploaded_csv)
    st.write("ファイルを処理。先頭5行はこちら：")
    st.write(df.head())

# 画像ファイルの処理
st.header("画像ファイル処理→グレー")
uploaded_img = st.file_uploader("画像ファイルをアップロードしてね", type=["png", "jpg", "jpeg"])

if uploaded_img is not None:
    image = Image.open(uploaded_img)
    gray_image = image.convert("L")
    st.write("画像をグレーに変換したよ。")
    st.image(gray_image)