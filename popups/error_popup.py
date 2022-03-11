from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

Builder.load_file("error_popup.kv")

class MyPopup(Popup):
    pass

class MyLayout(BoxLayout):
    pass

class MyApplication(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApplication().run()
