from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("file_chooser.kv")

class MyLayout(BoxLayout):
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            print(filename[0])
        except:
            print("error in the filename")

class MyApplication(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApplication().run()
