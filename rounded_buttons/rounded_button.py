from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget


Builder.load_file("rounded_button.kv")

class MyWidget(Widget):
    pass

class MyApplication(App):
    def build(self):
        return MyWidget()


if __name__ == "__main__":
    MyApplication().run()
