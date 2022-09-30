from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu

class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class MainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file("menu.kv")

        countries = ["India", "Denmark","Italy","Finland", "Sweden", "Brazil"]
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": c,
                "on_release": lambda x=c: self.set_item(x)
            } for c in countries
        ]

        self.menu = MDDropdownMenu(
            caller = self.screen.ids.drop_item,
            items = menu_items,
            position = "bottom",
            width_mult = 4
        )
        self.menu.bind()

    def set_item(self, text_item):
        self.screen.ids.drop_item.set_item(text_item)
        self.menu.dismiss()

    def build(self):
        return self.screen

if __name__ == "__main__":
    MainApp().run()
