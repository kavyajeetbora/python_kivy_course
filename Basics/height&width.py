import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class myApp(App):

    def build(self):

        self.main_window = GridLayout()
        self.main_window.cols=1
        ## intiate the layout, here we use grid type layout
        self.top_window = GridLayout()
        self.top_window.cols = 2
        self.main_window.add_widget(self.top_window)

        name_label = Label(
            text="Name:",
            font_size=12,
            size_hint_y = None,
            height = 50, ## units are in pixels
            size_hint_x = None,
            width = 200
        )
        self.top_window.add_widget(name_label)

        self.name_input = TextInput(
            multiline=False,
            size_hint_y = None,
            height = 50, ## units are in pixels
            size_hint_x = None,
            width = 200
        )
        self.top_window.add_widget(self.name_input)

        email_label = Label(text="email address:",font_size=12)
        self.top_window.add_widget(email_label)
        self.email_input = TextInput(multiline=False)
        self.top_window.add_widget(self.email_input)

        mobile_label = Label(text="Mobile Number:",font_size=12)
        self.top_window.add_widget(mobile_label)
        self.mobile_input = TextInput(multiline=False)
        self.top_window.add_widget(self.mobile_input)

        ## Create another grid for buttons
        self.bottom_window = GridLayout()
        self.main_window.add_widget(self.bottom_window)

        self.bottom_window.cols = 1
        self.output_label = Label()
        self.bottom_window.add_widget(self.output_label)
        self.button = Button(
            text="Submit",
            font_size=20,
            size_hint_y = None,
            height = 50, ## units are in pixels
            size_hint_x = None,
            width = 200
        )
        self.button.bind(on_press=self.submit)
        self.bottom_window.add_widget(self.button)

        return self.main_window

    def submit(self, instance):
        name = self.name_input.text
        email = self.email_input.text
        mobile = self.mobile_input.text
        if name != "" and email != "" and mobile != "":
            text = f"Hello {name}, your email id {email} and your mobile number is {mobile}"
            self.output_label.text = text
            self.name_input.text = ""
            self.email_input.text = ""
            self.mobile_input.text = ""
        else:
            self.output_label.text = "please enter the details!"

if __name__ == "__main__":
    application = myApp()
    application.run()
