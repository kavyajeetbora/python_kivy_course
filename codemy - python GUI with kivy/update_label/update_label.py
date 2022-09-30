from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder

Builder.load_file("update_label.kv")

class MyLayout(Widget):

    def press(self):
        ## create variables for out widgets
        name = self.ids.name_input.text
        ## update the Label
        self.ids.name_label.text = f"Hello {name}, welcome to this application"

        ## clear the input box
        self.ids.name_input.text = ""


class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()
