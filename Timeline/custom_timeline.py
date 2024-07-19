# custom_timeline.py
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Line


class CustomTimelineWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        with self.canvas.after:
            Color(0, 0, 1, 1)
            self.border_line = Line(rectangle=(self.x, self.y, self.width, self.height), width=2)

        scroll_view = ScrollView(do_scroll_x=False, do_scroll_y=True)

        self.bind(pos=self.update_border, size=self.update_border)

        # Day of the week row
        self.day_of_week_row = GridLayout(cols=7, size_hint=(1, 0.1))

        days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for day in days_of_week:
            day_label = Label(text=day)
            self.day_of_week_row.add_widget(day_label)

        scroll_view.add_widget(self.day_of_week_row) ## chng this

        # Add the ScrollView to the main layout
        self.add_widget(scroll_view)

    def update_border(self, *args):
        self.border_line.rectangle = (self.x, self.y, self.width, self.height)

def get_custom_timeline():
    return CustomTimelineWidget()
