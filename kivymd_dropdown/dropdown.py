from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu

class AppLayout(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        countries = ["India", "Denmark", "Italy"]
        menu_items = [
            {
                "viewclass": "OneLineIconListItem",
                "text" : i,
                "height": dp(56),
                "on_release": lambda x = i: self.set_item(x)
            } for i in countries
        ]

        self.country_menu = MDDropdownMenu(
            caller = self.ids.country,
            items = menu_items,
            position = "center",
            width_mult = 4
        )
        self.country_menu.bind()

    def set_item(self, country):
        self.ids.country.set_item(country)
        self.country_menu.dismiss()

class MainApp(MDApp):

    def build(self):
        Builder.load_file("dropdown.kv")
        return AppLayout()

if __name__ == "__main__":
    MainApp().run()
