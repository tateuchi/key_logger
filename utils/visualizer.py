import matplotlib.pyplot as plt
import japanize_matplotlib

def plot_data(filtered_data):
    # 打鍵回数でソート
    sorted_data = sorted(filtered_data.items(), key=lambda x: x[1])
    
    # キーと回数を分離
    keys = [item[0] for item in sorted_data]
    counts = [item[1] for item in sorted_data]
    
    # グラフの描画
    plt.figure(figsize=(12, max(len(keys) * 0.4, 6)))  # 縦方向のスペースを動的に調整
    bars = plt.barh(keys, counts)  # 横棒グラフ
    plt.xlabel("Count", fontsize=12)
    plt.ylabel("Keys", fontsize=12)
    plt.title("Key Usage Frequency (Sorted)", fontsize=14)

    # 棒の上に値ラベルを表示
    for bar, count in zip(bars, counts):
        plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,  # ラベルの位置調整
                 str(count), va='center', fontsize=10)

    # 軸のスペース調整
    plt.subplots_adjust(left=0.35, right=0.95, top=0.9, bottom=0.1)  # ラベルの見やすさを調整
    
    # Y軸のラベルが多い場合、フォントサイズを自動調整
    max_label_len = max([len(str(key)) for key in keys])
    if len(keys) > 20 or max_label_len > 15:
        plt.yticks(fontsize=8)
    else:
        plt.yticks(fontsize=12)

    # グラフを表示
    plt.show()

def display_ranking(filtered_data, top_n=10):
    """
    使用頻度ランキングを表示する関数。
    :param filtered_data: キーの使用データ (辞書形式)
    :param top_n: 表示する上位ランキング数
    """
    # データ変換
    try:
        data = {key: value["count"] if isinstance(value, dict) else value for key, value in filtered_data.items()}
    except KeyError as e:
        raise ValueError(f"Invalid data format: {filtered_data}. Error: {e}")

    # 打鍵回数でソート
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

    # ランキング表示
    print("\n=== 使用頻度ランキング ===")
    for i, (key, count) in enumerate(sorted_data[:top_n], start=1):
        print(f"{i}. Key: {key} - Count: {count}")
    print("========================\n")
