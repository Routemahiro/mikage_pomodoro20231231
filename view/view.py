# view.py
import tkinter as tk
from model.timer import Timer

class TimerView:
    def __init__(self, master, start_callback, update_callback):
        timer = Timer()  # Timerクラスのインスタンスを作成
        initial_time = timer.get_work_time()  # work_timeを取得

        self.master = master
        self.start_callback = start_callback
        self.update_callback = update_callback

        self.time_label = tk.Label(master, font=("Helvetica", 36))
        self.time_label.pack()
        self.update_time_display(initial_time)  # 初期時間を設定

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

    def start_timer(self):
        self.start_callback()

    def update_time_display(self, time):
        self.time_label.config(text=time)