from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.core.window import Window
from screeninfo import get_monitors
from calendar import monthrange

import sqlite3


# Get screen size
monitor = get_monitors()[0]
width, height = monitor.width, monitor.height

# Set the window size to 1/3 of the screen width and full height
Config.set('graphics', 'borderless', '1')

def get_tasks_for_day(date):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT task FROM tasks WHERE date = ?", (date,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

class Calendar(GridLayout):
    def __init__(self, **kwargs):
        super(Calendar, self).__init__(**kwargs)
        self.cols = 7
        self.update_calendar(2022, 'January')

    def update_calendar(self, year, month):
        self.clear_widgets()  # Remove existing buttons
        month_number = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                        'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}[month]
        days_in_month = monthrange(year, month_number)[1]
        for day in range(1, days_in_month + 1):
            date_str = f"{year}-{month_number:02d}-{day:02d}"
            btn = Button(text=str(day))
            btn.bind(on_press=lambda instance, date=date_str: self.show_tasks_for_day(date))
            self.add_widget(btn)

    def show_tasks_for_day(self, date):
        tasks = get_tasks_for_day(date)
        # Here you can update your UI to show the tasks or print them to the console
        print(f"Tasks for {date}: {tasks}")


class MyApp(App):
    def build(self):
        # Set the size of the window
        Window.size = (width // 3, height)
        # Set the position of the window to (0, 0)
        Window.top = 0
        Window.left = 2 * (width // 3)
        
        layout = BoxLayout(orientation='vertical')
        self.calendar = Calendar(size_hint=(1, 0.33))
        spacer = Widget()
        
        self.year_spinner = Spinner(
            text='2022',
            values=[str(i) for i in range(2022, 2030)],
            size_hint=(1, 0.1)
        )
        self.month_spinner = Spinner(
            text='January',
            values=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            size_hint=(1, 0.1)
        )
        
        self.year_spinner.bind(text=self.update_calendar)
        self.month_spinner.bind(text=self.update_calendar)
        
        layout.add_widget(self.year_spinner)
        layout.add_widget(self.month_spinner)
        layout.add_widget(self.calendar)
        layout.add_widget(spacer)
        
        return layout

    def update_calendar(self, instance, value):
        year = int(self.year_spinner.text)
        month = self.month_spinner.text
        self.calendar.update_calendar(year, month)

if __name__ == '__main__':
    MyApp().run()