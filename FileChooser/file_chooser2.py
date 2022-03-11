from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.filechooser import FileChooserIconView, FileChooserListView
from kivy.properties import ObjectProperty
from kivymd.app import MDApp

Builder.load_file("file_chooser2.kv")

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_chooser = ObjectProperty()
        self.file_browser_popup = ObjectProperty()

    def choose_file(self):

        layout = BoxLayout(orientation = "vertical", spacing=20)
        label = MDLabel(text = "Choose a file to upload:", halign="center")
        button = MDRaisedButton(text = "Select a File", pos_hint = {"center_x":0.5})
        self.file_chooser = FileChooserListView()
        close_button = MDRaisedButton(text = "Cancel", pos_hint = {"center_x":0.5})

        layout.add_widget(self.file_chooser)
        layout.add_widget(button)
        layout.add_widget(close_button)
        # layout.add_widget(Widget())

        self.file_browser_popup = Popup(title = "File Explorer", content = layout)
        self.file_browser_popup.open()

        button.bind(on_press = self.select_file)
        close_button.bind(on_press = self.file_browser_popup.dismiss)

    def select_file(self, instance):
        if len(self.file_chooser.selection) == 1:
            self.ids.filename.text = f"uploaded file: {self.file_chooser.selection[0]}"
        else:
            self.ids.filename.text = ""

        self.file_browser_popup.dismiss()

class MyApplication(MDApp):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApplication().run()
