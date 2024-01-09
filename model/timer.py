# timer.py
class Timer:
    def __init__(self):
        # self.work_time = 2 * 10
        # self.break_time = 1 * 10
        self.work_time = 3
        self.break_time = 2
        self.current_time = self.work_time
        self.running = False
        self.is_work_time = True

    def time_format(self, time_in_sec):
        minutes, seconds = divmod(time_in_sec, 60)
        return f"{minutes:02}:{seconds:02}"

    def update_timer(self):
        if self.running and self.current_time > 0:
            self.current_time -= 1
        elif self.running and self.current_time == 0:
            self.running = False  # セッションが終了したら自動的には次のセッションに移行しない


    def get_work_time(self):
        return self.time_format(self.work_time)