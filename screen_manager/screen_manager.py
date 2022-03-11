from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

class MyLayout(BoxLayout):
    pass

class MyApplication(MDApp):
    def build(self):
        Builder.load_file("screen_manager.kv")
        return MyLayout()

if __name__ == "__main__":
    MyApplication().run()
