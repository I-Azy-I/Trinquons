# -- encoding: utf-8 --
import json
import data
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout  # one of many layout structures
from kivy.uix.textinput import TextInput  # allow for ...text input.
from kivy.uix.button import Button
kivy.require("1.11.1")

# An actual app is likely to consist of many different
# "pages" or "screens." Inherit from GridLayout
class ConnectPage(GridLayout):
    # runs on initialization
    def __init__(self, **kwargs):
        # we want to run __init__ of both ConnectPage AAAAND GridLayout (understanding_super.py)
        super().__init__(**kwargs)

        self.cols = 1
        self.text=Label(text='Trinquons!')
        self.add_widget(self.text)  # used for our grid
        self.button = Button()
        self.button.bind(on_press=self.button_get_text) # just take up the spot.
        self.add_widget(self.button)

    def button_get_text(self, instance):
        text=test.get_text()
        self.text.text=f"Trinquon pour la fête nationale de {text[0]}"

        # widgets added in order, so mind the order.



class EpicApp(App):
    def build(self):
        return ConnectPage()


if __name__ == "__main__":
    test= data.Text_generator()
    test.init()
    EpicApp().run()
