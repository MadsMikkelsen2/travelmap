# 必要なライブラリをインポートする
import streamlit as st
import requests

# Streamlitアプリケーションのタイトルを設定する
st.title('現在地を地図上に表示する')

# IPアドレスを取得するAPIのURL
ip_api_url = 'https://api.ipify.org?format=json'

# IPアドレスを取得する関数
def get_ip():
    response = requests.get(ip_api_url)
    ip_data = response.json()
    return ip_data['ip'] if 'ip' in ip_data else None

# IPアドレスから現在の位置情報を取得するAPIのURL
location_api_url = 'http://ip-api.com/json/'

# 現在の位置情報を取得する関数
def get_location(ip):
    response = requests.get(location_api_url + ip)
    location_data = response.json()
    return location_data

# 現在のIPアドレスを取得する
ip_address = get_ip()

# IPアドレスが取得できた場合
if ip_address:
    # 現在の位置情報を取得する
    location_data = get_location(ip_address)
    
    # 地図を表示する
    st.map((location_data['lat'], location_data['lon']))

    # 位置情報の詳細を表示する
    st.write(f'現在地の情報
