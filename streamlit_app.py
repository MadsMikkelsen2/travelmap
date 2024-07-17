# 必要なライブラリをインポートする
import streamlit as st
import random

# ページのタイトルを設定する
st.title('サイコロシミュレータ')

# ヘッダーを表示する
st.header('サイコロを振ろう！')

# 「振る」ボタンを作成する
if st.button('振る'):
    # 1から6の間のランダムな整数を生成する
    dice_value = random.randint(1, 6)
    # サイコロの出目を表示する
    st.write(f'出た目は: {dice_value}')

