# controller.py
from model.timer import Timer
from view.view import TimerView
import tkinter as tk

class TimerController:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Timer()
        self.view = TimerView(self.root, self.start_timer, self.update_time_display)
        self.timer_id = None

    def start_timer(self):
        if not self.model.running:
            self.model.running = True
            self.view.start_button.config(text="Pause")
            self.update_time_display()
        else:
            self.model.running = False
            self.view.start_button.config(text="Start")
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
                self.timer_id = None
            self.model.is_work_time = not self.model.is_work_time  # セッションが終了したら次のセッションに切り替える
            self.model.current_time = self.model.work_time if self.model.is_work_time else self.model.break_time  # 次のセッションの時間を設定
            self.view.update_time_display(self.model.time_format(self.model.current_time))  # 次のセッションの時間を表示

    def update_time_display(self):
        if self.model.running and self.model.current_time > 0:
            self.view.update_time_display(self.model.time_format(self.model.current_time))
            self.model.update_timer()
            self.timer_id = self.root.after(1000, self.update_time_display)
        elif self.model.running and self.model.current_time == 0:
            self.start_timer()  # セッションが終了したら自動的には次のセッションに移行しない

    def run(self):
        self.root.mainloop()