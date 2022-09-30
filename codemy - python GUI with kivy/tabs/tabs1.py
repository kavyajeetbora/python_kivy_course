from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file("tabs1.kv")

class MyLayout(TabbedPanel):
    pass

class Application(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    Application().run()
