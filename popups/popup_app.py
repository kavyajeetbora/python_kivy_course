from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.popup import Popup

Builder.load_file("popup_design.kv")
file_name = StringProperty()

class MyPopup(Popup):
    def select_file(self, filename):
        file_name = filename
        self.dismiss()

class MyLayout(BoxLayout):
    pass

class MyApplication(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApplication().run()
