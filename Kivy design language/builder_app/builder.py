from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("color.kv")

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    email = ObjectProperty(None)
    phone = ObjectProperty(None)

    def submit(self):
        name = self.name.text
        email = self.email.text
        phone = self.phone.text

        print(f"Your name is {name}.\nYour email id is {email} and your phone number is {phone}.")

        self.name = ""
        self.email = ""
        self.phone = ""

class AwesomeApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    AwesomeApp().run()
