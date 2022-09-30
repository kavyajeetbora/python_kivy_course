from kivy.lang import Builder
from kivymd.app import MDApp


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_file('themes_kivymd.kv')


if __name__ == "__main__":
    MyApp().run()
