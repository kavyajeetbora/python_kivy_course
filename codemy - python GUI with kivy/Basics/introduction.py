import kivy
from kivy.app import App
from kivy.uix.label import Label

class myApp(App):

    def build(self):
        label = Label(
            text="Hello World",
            font_size=72
        )

        return label

if __name__ == "__main__":
    application = myApp()
    application.run()
