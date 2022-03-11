from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class Application(MDApp):
    def build(self):
        return Builder.load_file("tabs.kv")

    def on_start(self):
        all_tabs = ["General Data", "Limit State Info", "Capacity Info", "Load Input", "Over view", "Result"]
        for i in all_tabs:
            self.root.ids.tabs.add_widget(
                Tab(title=i)
            )

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        instance_tab.ids.label.text = tab_text


if __name__ == "__main__":
    Application().run()
