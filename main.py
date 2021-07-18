from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from datetime import datetime
from kivy.clock import Clock


from kivy.config import Config
Config.set('graphics','resizable',0)


class ClockUI(BoxLayout):
    
    def update(self,dt):
        date = datetime.today()
        self.ids.date.text=f"{date:%B %d, %Y}"
        self.ids.weekday.text=f"{date:%A}"        
        self.ids.time.text=f"{date.hour:02d}:{date.minute:02d}:{date.second:02d} {'AM' if date.hour<12 else 'PM'}"


class ClockApp(App):
    def build(self):
        clockui = ClockUI()
        Clock.schedule_interval(clockui.update,1.0/32.0)
        Window.size=(350,200)
        self.icon = "clockicon.ico"
        print(self.get_application_icon())
        return clockui

if __name__ == "__main__":
    clock = ClockApp()
    clock.run()