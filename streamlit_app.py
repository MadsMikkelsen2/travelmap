
import geocoder

def get_current_location():
    g = geocoder.ip('me')
    return g.latlng

def main():
    location = get_current_location()
    if location:
        latitude, longitude = location
        print(f"現在の緯度: {latitude}, 経度: {longitude}")
    else:
        print("位置情報を取得できませんでした。")

if __name__ == "__main__":
    main()
