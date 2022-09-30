from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("checkboxes.kv")

class MyWidget(Widget):

    teams = []

    def checkbox_click(self, instance, value, team):
        if value:
            MyWidget.teams.append(team)
            self.ids.output_label.text =  " & ".join(MyWidget.teams)

        else:
            MyWidget.teams.remove(team)
            if len(team)>1:
                delimiter = " & "
            else:
                delimiter = " "
            self.ids.output_label.text = delimiter.join(MyWidget.teams)

class MyApplication(App):
    def build(self):
        return MyWidget()

if __name__ == "__main__":
    MyApplication().run()
