# 必要なライブラリをインポートする
import streamlit as st
import requests

# Streamlitアプリケーションのタイトルを設定する
st.title('現在地を地図上に表示する')


# 現在の位置情報を取得するAPIのURL
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
ip_address = get_ip()

# IPアドレスが取得できた場合
if ip_address:
    # 現在の位置情報を取得する
    location_data = get_location(ip_address)
    
    if location_data:
        # 地図を表示する
        st.map((location_data['lat'], location_data['lon']))
        
        # 位置情報の詳細を表示する
        st.write(f'現在地の情報:')
        st.write(f'都市: {location_data["city"]}')
        st.write(f'国: {location_data["country"]}')
        st.write(f'緯度: {location_data["lat"]}')
        st.write(f'経度: {location_data["lon"]}')
        st.write(f'ISP: {location_data["isp"]}')
    else:
        st.write('位置情報が取得できませんでした。')
else:
    st.write('IPアドレスが取得できませんでした。')

