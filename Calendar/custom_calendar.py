# custom_calendar.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty

from datetime import datetime, timedelta
import math

class CustomCalendarWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Month and Year selection
        self.month_year_spinner = Spinner(
            text='January 2024',
            values=[(datetime(2024, i, 1).strftime('%B %Y')) for i in range(1, 13)],
            size_hint=(1, 0.1)
        )
        self.month_year_spinner.bind(text=self.update_calendar)
        self.add_widget(self.month_year_spinner)

        # Day of the week row
        self.day_of_week_row = GridLayout(cols=7, size_hint=(1, 0.1))
        
        self.add_widget(self.day_of_week_row)

        days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        for day in days_of_week:
            day_label = Label(text=day)
            self.day_of_week_row.add_widget(day_label)

        # Calendar grid for dates
        self.calendar_grid = GridLayout(cols=7, rows=5, size_hint=(1, 0.6))
        self.add_widget(self.calendar_grid)
        self.update_calendar()  # Initial population of the calendar
        

    def update_calendar(self, *args):
        self.calendar_grid.clear_widgets()  # Clear existing date buttons

        selected_month, selected_year = self.month_year_spinner.text.split(' ')
        print(f'Selected Month and Year: {selected_month} {selected_year}')  # Print the selected month and year
        month = datetime.strptime(selected_month, '%B').month
        year = int(selected_year)
        num_days = (datetime(year, month % 12 + 1, 1) - timedelta(days=1)).day
        #print(num_days)

        for day in range(1, num_days + 1):
            # Customize the additional_text as per your requirement
            additional_text = "Info"  # Example additional text
            date_button = CustomDateButton(date_text=str(day), additional_text=additional_text)
            self.calendar_grid.add_widget(date_button)
  
class CustomDateButton(Button):
    def __init__(self, date_text, additional_text="", **kwargs):
        super().__init__(**kwargs)
        self.text = f"{date_text}\n{additional_text}"

def get_custom_calendar():
    return CustomCalendarWidget()