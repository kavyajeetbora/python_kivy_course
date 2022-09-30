from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt

from kivymd.app import MDApp
from kivy.lang import Builder

plt.plot([1,2,3,4,5])
plt.ylabel("some numbers")

class MyApp(MDApp):
    def on_start(self):
        self.screen = Builder.load_file("graph_app.kv")

    def build(self):
        box = BoxLayout()
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        return box

if __name__ == "__main__":
    MyApp().run()
