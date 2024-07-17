import time

def print_clock():
    while True:
        # 現在の時刻を取得
        current_time = time.strftime("%H:%M:%S", time.localtime())
        # ターミナルに時刻を表示（上書きして更新）
        print(f"\r{current_time}", end="", flush=True)
        # 1秒ごとに更新
        time.sleep(1)

if __name__ == "__main__":
    print_clock()
