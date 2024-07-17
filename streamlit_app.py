# 必要なライブラリをインポートする
import streamlit as st
import folium
from streamlit_folium import folium_static  # 必要に応じて追加

# 以下にアプリケーションのコードを記述します


# Streamlitアプリケーションのタイトルを設定する
st.title('日本地図を表示する')

# 日本の中心座標を指定する（おおよその位置）
japan_center = (36.2048, 138.2529)

# Foliumの地図オブジェクトを作成する
m = folium.Map(location=japan_center, zoom_start=6)

# Streamlitのウィジェットに地図を表示する
folium_static(m)




# 地図を作成する
m = folium.Map(location=[36.2048, 138.2529], zoom_start=5)  # 初期位置を日本の中心に設定する

# 各都市のマーカーを地図に追加する
for city, coord in cities.items():
    folium.Marker(coord, popup=city).add_to(m)

# Streamlitで地図を表示する
folium_static(m)
