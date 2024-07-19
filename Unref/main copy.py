from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.core.window import Window
from screeninfo import get_monitors

# Get screen size
monitor = get_monitors()[0]
width, height = monitor.width, monitor.height

# Set the window size to 1/3 of the screen width and full height
Config.set('graphics', 'borderless', '1')

class Calendar(GridLayout):
    def __init__(self, **kwargs):
        super(Calendar, self).__init__(**kwargs)
        self.cols = 7
        for i in range(1, 31):
            btn = Button(text=str(i))
            self.add_widget(btn)

class MyApp(App):
    def build(self):
        # Set the size of the window
        Window.size = (width // 3, height)
        # Set the position of the window to (0, 0)
        Window.top = 0
        Window.left = 2 * (width // 3)
        
        layout = BoxLayout(orientation='vertical')
        calendar = Calendar(size_hint=(1, 0.33))
        spacer = Widget()
        
        year_spinner = Spinner(
            text='2022',
            values=[str(i) for i in range(2000, 2030)],
            size_hint=(1, 0.1)
        )
        month_spinner = Spinner(
            text='January',
            values=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            size_hint=(1, 0.1)
        )
        
        layout.add_widget(year_spinner)
        layout.add_widget(month_spinner)
        layout.add_widget(calendar)
        layout.add_widget(spacer)
        
        return layout

if __name__ == '__main__':
    MyApp().run()