# 必要なライブラリをインポートする
import streamlit as st
import requests
import folium
from streamlit_folium import folium_static

# Streamlitアプリケーションのタイトルを設定する
st.title('現在の位置を地図上に表示する')

# IP-APIのURL
location_api_url = 'http://ip-api.com/json/'

# 現在の位置情報を取得する関数
def get_location(ip):
    response = requests.get(location_api_url + ip)
    if response.status_code == 200:
        location_data = response.json()
        return location_data
    else:
        st.error(f'位置情報を取得できませんでした。ステータスコード: {response.status_code}')
        return None

# 現在のIPアドレスを取得する
ip_address = st.experimental_get_query_params().get('ip', None) or st.experimental_get_query_params().get('ip_address', None)
if ip_address is None:
    ip_address = st.experimental_get_query_params().get('ip', None) or st.experimental_get_query_params().get('ip_address', None)
    if not ip_address:
        ip_address = get_ip_address()
    デフ゛

