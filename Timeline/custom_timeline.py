# custom_timeline.py
from kivy.uix.button import Button 
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Line,Rectangle
from kivy.properties import NumericProperty
class SyncedScrollView(ScrollView):
    scroll_y = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bar_width = 0  # Turn off the scroll indicator

    def on_scroll_y(self, instance, value):
        # When this view is scrolled, update its pair
        if hasattr(self, 'pair'):
            self.pair.scroll_y = value

    def on_touch_up(self, touch):
        # Ensure scroll_y is updated on touch up
        super().on_touch_up(touch)
        if self.collide_point(*touch.pos):
            self.on_scroll_y(self, self.scroll_y)

class CustomTimelineWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Colors
        self.axis_color = (0, 0, 0.5, 1)  # Dark blue
        self.grid_color = (0.9, 0.9, 0.9, 1)  # Light gray

        # Day of the week row (fixed at the top)
        self.day_of_week_row = GridLayout(cols=8, size_hint_y=None, height=40)
        days_of_week = ['Time', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for day in days_of_week:
            day_label = Label(text=day)
            with day_label.canvas.before:
                Color(*self.axis_color)
                Rectangle(pos=day_label.pos, size=day_label.size)
            day_label.bind(pos=self.update_rect, size=self.update_rect)
            self.day_of_week_row.add_widget(day_label)

        # Main content area
        content_layout = BoxLayout(orientation='horizontal')

        # Time axis scroll view
        time_scroll = SyncedScrollView(size_hint_x=None, width=60, do_scroll_x=False)
        time_grid = GridLayout(cols=1, size_hint_y=None)
        time_grid.bind(minimum_height=time_grid.setter('height'))

        # Main grid scroll view
        main_scroll = SyncedScrollView(do_scroll_x=False)
        main_grid = GridLayout(cols=7, size_hint_y=None, spacing=1)
        main_grid.bind(minimum_height=main_grid.setter('height'))

        # Link the two scroll views
        time_scroll.pair = main_scroll
        main_scroll.pair = time_scroll

        # Populate time axis and main grid
        for i in range(24):
            # Time label
            time_label = Label(text=f'{i:02d}:00', size_hint_y=None, height=40)
            with time_label.canvas.before:
                Color(*self.axis_color)
                Rectangle(pos=time_label.pos, size=time_label.size)
            time_label.bind(pos=self.update_rect, size=self.update_rect)
            time_grid.add_widget(time_label)

            # Day slots
            for _ in range(7):  # 7 days
                slot = Label(text="", size_hint_y=None, height=40)
                with slot.canvas.before:
                    Color(*self.grid_color)
                    Rectangle(pos=slot.pos, size=slot.size)
                slot.bind(pos=self.update_rect, size=self.update_rect)
                main_grid.add_widget(slot)

        time_scroll.add_widget(time_grid)
        main_scroll.add_widget(main_grid)

        content_layout.add_widget(time_scroll)
        content_layout.add_widget(main_scroll)

        # Add widgets to the main layout
        self.add_widget(self.day_of_week_row)
        self.add_widget(content_layout)

    def update_rect(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            if instance.text in ['Time'] or ':' in instance.text:  # Time labels
                Color(*self.axis_color)
            else:  # Day slots
                Color(*self.grid_color)
            Rectangle(pos=instance.pos, size=instance.size)

def get_custom_timeline():
    return CustomTimelineWidget()
