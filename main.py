from utils.data_handler import filter_data, load_data, get_date_range
from utils.visualizer import plot_data, display_ranking
from tkinter import Tk, Label, Button, Entry
from datetime import datetime

def show_gui():
    def on_submit():
        # 入力された日付を取得
        start_date_input = start_entry.get()
        end_date_input = end_entry.get()

        # デフォルトの日付範囲を取得
        all_data = load_data()
        default_start_date, default_end_date = get_date_range(all_data)

        if default_start_date is None or default_end_date is None:
            print("No data available.")
            return

        # 入力が空の場合、デフォルト値を使用
        start_date = datetime.strptime(start_date_input, '%Y-%m-%d') if start_date_input else default_start_date
        end_date = datetime.strptime(end_date_input, '%Y-%m-%d') if end_date_input else default_end_date

        # データのフィルタリングと表示
        filtered = filter_data(start_date, end_date)
        display_ranking(filtered)
        plot_data(filtered)

    root = Tk()
    root.title("Key Usage Analysis")

    Label(root, text="Start Date (YYYY-MM-DD, leave empty for default):").pack()
    start_entry = Entry(root)
    start_entry.pack()

    Label(root, text="End Date (YYYY-MM-DD, leave empty for default):").pack()
    end_entry = Entry(root)
    end_entry.pack()

    Button(root, text="Analyze", command=on_submit).pack()

    root.mainloop()

if __name__ == "__main__":
    show_gui()
