from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


class MyLayout(MDBoxLayout):
    def activate_radio(self, instance, value):
        print(instance, value)

class Application(MDApp):
    def build(self):
        Builder.load_file("check_box.kv")
        return MyLayout()

if __name__ == "__main__":
    Application().run()
