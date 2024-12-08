from utils.data_handler import filter_data
from utils.visualizer import plot_data
from tkinter import Tk, Label, Button, Entry
from datetime import datetime

def show_gui():
    def on_submit():
        start_date = datetime.strptime(start_entry.get(), '%Y-%m-%d')
        end_date = datetime.strptime(end_entry.get(), '%Y-%m-%d')
        filtered = filter_data(start_date, end_date)
        plot_data(filtered)

    root = Tk()
    root.title("Key Usage Analysis")

    Label(root, text="Start Date (YYYY-MM-DD):").pack()
    start_entry = Entry(root)
    start_entry.pack()

    Label(root, text="End Date (YYYY-MM-DD):").pack()
    end_entry = Entry(root)
    end_entry.pack()

    Button(root, text="Analyze", command=on_submit).pack()

    root.mainloop()

if __name__ == "__main__":
    show_gui()
