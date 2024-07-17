import folium
import geocoder

# 現在の位置情報を取得
def get_current_location():
    # geocoderを使用してIPアドレスから位置情報を取得する例
    g = geocoder.ip('me')
    return g.latlng

# 地図を作成する関数
def create_map(location):
    # locationは緯度(latitude)と経度(longitude)のペア
    map = folium.Map(location=location, zoom_start=15)
    folium.Marker(location=location, popup='現在地', tooltip='クリックして詳細を表示').add_to(map)
    return map

def main():
    # 現在の位置情報を取得
    location = get_current_location()
    
    # 地図を作成
    map = create_map(location)
    
    # 地図をHTMLファイルとして保存（任意）
    map.save('current_location_map.html')

    # 地図を表示（ブラウザで開く）
    map.show()

if __name__ == "__main__":
    main()

