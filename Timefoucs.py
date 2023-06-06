import tkinter as tk
from tkinter import messagebox

class PomodoroTimer:
    def __init__(self, minutes):
        self.minutes = minutes
        self.seconds = minutes * 60
        self.is_running = False
        self.window = tk.Tk()
        self.window.title("专注时钟")
        self.label = tk.Label(self.window, text="")
        self.label.pack(pady=10)
        self.start_button = tk.Button(self.window, text="开始", command=self.start_timer)
        self.start_button.pack(pady=5)
        self.stop_button = tk.Button(self.window, text="停止", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

    def start_timer(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        while self.seconds >= 0 and self.is_running:
            self.update_label()
            self.window.update()
            time.sleep(1)
            self.seconds -= 1
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        messagebox.showinfo("时间到", "专注时间已结束！")

    def stop_timer(self):
        self.is_running = False

    def update_label(self):
        mins, secs = divmod(self.seconds, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        self.label.config(text=timer)

    def run(self):
        self.window.mainloop()

def main():
    print("欢迎使用专注时钟！")
    minutes = int(input("请输入专注时长（以分钟为单位）："))
    timer = PomodoroTimer(minutes)
    timer.run()

if __name__ == "__main__":
    main()
