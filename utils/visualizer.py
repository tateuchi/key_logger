import matplotlib.pyplot as plt

def plot_data(filtered_data):
    # 打鍵回数でソート
    sorted_data = sorted(filtered_data.items(), key=lambda x: x[1])
    
    # キーと回数を分離
    keys = [item[0] for item in sorted_data]
    counts = [item[1] for item in sorted_data]
    
    # グラフの描画
    plt.figure(figsize=(10, len(keys) * 0.5))  # 縦方向のスペースを調整
    plt.barh(keys, counts)  # 横棒グラフ
    plt.xlabel("Count")
    plt.ylabel("Keys")
    plt.title("Key Usage Frequency (Sorted)")
    
    # 軸のスペース調整
    plt.subplots_adjust(left=0.25, right=0.95, top=0.9, bottom=0.1)  # ラベルの見やすさを調整
    plt.xticks(fontsize=10)  # 横軸のフォントサイズ
    plt.yticks(fontsize=12)  # 縦軸のフォントサイズ
    
    # 各棒に値ラベルを表示
    for i, count in enumerate(counts):
        plt.text(count + 0.5, i, str(count), va='center', fontsize=10)
    
    plt.show()

def display_ranking(filtered_data, top_n=5):
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
