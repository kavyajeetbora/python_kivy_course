from kivymd.app import MDApp
from kivy.lang import Builder

class Application(MDApp):
    def build(self):
        ## set the theme
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file("design.kv")

    def log_in(self):
        self.root.ids.welcome_label.text = f"Hello {self.root.ids.user.text}\nEmail ID is {self.root.ids.email.text}"
        
    def clear(self):
        self.root.ids.welcome_label.text = "Welcome to KivyMD library"
        self.root.ids.user.text = ""
        self.root.ids.email.text = ""

if __name__ == "__main__":
    Application().run()
