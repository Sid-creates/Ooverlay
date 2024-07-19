import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime, timedelta

class CalendarTimelineUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar, Timeline, and Input UI")
        self.master.geometry("800x600")

        # Create main frame
        self.main_frame = ttk.Frame(self.master, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create three columns
        self.calendar_frame = ttk.Frame(self.main_frame, width=300, relief=tk.RIDGE, padding="5")
        self.timeline_frame = ttk.Frame(self.main_frame, width=300, relief=tk.RIDGE, padding="5")
        self.input_frame = ttk.Frame(self.main_frame, width=200, relief=tk.RIDGE, padding="5")

        self.calendar_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.timeline_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.setup_calendar()
        self.setup_timeline()
        self.setup_input()

    def setup_calendar(self):
        self.current_date = datetime.now()
        
        # Calendar navigation
        nav_frame = ttk.Frame(self.calendar_frame)
        nav_frame.pack(fill=tk.X)

        ttk.Button(nav_frame, text="<", command=self.prev_month).pack(side=tk.LEFT)
        self.month_label = ttk.Label(nav_frame, text="")
        self.month_label.pack(side=tk.LEFT, expand=True)
        ttk.Button(nav_frame, text=">", command=self.next_month).pack(side=tk.RIGHT)

        # Calendar
        self.cal_frame = ttk.Frame(self.calendar_frame)
        self.cal_frame.pack(fill=tk.BOTH, expand=True)

        self.update_calendar()

    def update_calendar(self):
        for widget in self.cal_frame.winfo_children():
            widget.destroy()

        year = self.current_date.year
        month = self.current_date.month
        self.month_label.config(text=f"{calendar.month_name[month]} {year}")

        cal = calendar.monthcalendar(year, month)

        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for i, day in enumerate(days):
            ttk.Label(self.cal_frame, text=day).grid(row=0, column=i, padx=5, pady=5)

        for week_num, week in enumerate(cal, 1):
            for day_num, day in enumerate(week):
                if day != 0:
                    ttk.Button(self.cal_frame, text=str(day), width=4).grid(row=week_num, column=day_num, padx=1, pady=1)

    def prev_month(self):
        self.current_date = self.current_date.replace(day=1) - timedelta(days=1)
        self.update_calendar()

    def next_month(self):
        self.current_date = self.current_date.replace(day=28) + timedelta(days=5)
        self.current_date = self.current_date.replace(day=1)
        self.update_calendar()

    def setup_timeline(self):
        ttk.Label(self.timeline_frame, text="Timeline").pack()
        canvas = tk.Canvas(self.timeline_frame)
        canvas.pack(fill=tk.BOTH, expand=True)

        for hour in range(6, 24):
            y = (hour - 6) * 20
            canvas.create_line(0, y, 300, y, fill="gray")
            canvas.create_text(10, y, text=f"{hour:02d}:00", anchor="w")

    def setup_input(self):
        ttk.Label(self.input_frame, text="Enter data:").pack(pady=(0, 5))
        self.input_text = tk.Text(self.input_frame, height=5)
        self.input_text.pack(fill=tk.X, pady=(0, 5))
        ttk.Button(self.input_frame, text="Submit", command=self.submit_data).pack()

    def submit_data(self):
        data = self.input_text.get("1.0", tk.END).strip()
        if data:
            print(f"Submitted: {data}")
            self.input_text.delete("1.0", tk.END)

def main():
    root = tk.Tk()
    CalendarTimelineUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()