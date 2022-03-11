from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog


class MyLayout(BoxLayout):
    def press(self):
        dialog = MDDialog(
            title = "ERROR",
            text = "Error message"
        )
        dialog.open()

class MyApplication(MDApp):
    def build(self):
        Builder.load_file("alert_box.kv")
        return MyLayout()

if __name__ == "__main__":
    MyApplication().run()
