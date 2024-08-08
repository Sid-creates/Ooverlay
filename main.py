from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.core.window import Window
from screeninfo import get_monitors

# Import the helper function
from Calendar.custom_calendar import get_custom_calendar
from Timeline.custom_timeline import get_custom_timeline

# Assuming get_monitors() is defined elsewhere and works as expected
monitor = get_monitors()[0]
width, height = monitor.width, monitor.height

# Set the window size to 1/3 of the screen width and full height
Config.set('graphics', 'borderless', '1')

class MyApp(App):
    def build(self):
        # Set the size of the window
        Window.size = (width // 3, height)

        # Set the position of the window to the right third of the screen
        Window.top = 0
        Window.left = 2 * (width // 3)

        # Create a vertical BoxLayout
        layout = BoxLayout(orientation='vertical')

        # Use the helper function to add the custom calendar widget
        calendar = get_custom_calendar()
        layout.add_widget(calendar)

        # Use the helper function to add the custom calendar widget
        timeline = get_custom_timeline()
        layout.add_widget(timeline)   

        # Use the helper function to add the custom task display widget, currently spacer buttons
        button = Button(text=f'Button 3') 
        layout.add_widget(button)

        return layout

if __name__ == '__main__':
    MyApp().run()