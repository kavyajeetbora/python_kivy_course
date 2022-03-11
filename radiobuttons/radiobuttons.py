from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("radiobuttons.kv")

class MyWidget(Widget):

    def radio_button(self, instance, value, team):
        '''Arguments:
        1. instance is the radio button
        2. value is true or false (activated status)
        3. team user defined input
        '''
        if value:
            self.ids.output_label.text =  team
        else:
            self.ids.output_label.text = "None"

class MyApplication(App):
    def build(self):
        return MyWidget()

if __name__ == "__main__":
    MyApplication().run()
