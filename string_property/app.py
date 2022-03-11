from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.properties import StringProperty

Builder.load_file("app.kv")
class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = StringProperty(text="Hello world")
        
    def click(self):
        self.ids.label.text = self.text

class Application(MDApp):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    Application().run()
