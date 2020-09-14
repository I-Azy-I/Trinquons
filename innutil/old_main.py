# -- encoding: utf-8 --
import data
import text_editor
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
        self.add_widget(self.text)
        self.add_widget(Label())  # used for our grid
        self.button = Button()
        self.button.bind(on_press=self.button_get_text) # just take up the spot.
        self.add_widget(self.button)
        self.input= TextInput()
        self.add_widget(self.input)

    def button_get_text(self, instance):
        if self.input.text=="":
            data=pointeur.get_text()
        else:
            data=pointeur.get_text(self.input.text)
        text=data[1]
        tag=data[0]
        self.text.text=data[0]
        try :
            self.text.text=text_editor.text_affiche(tag,text)
        except:
            pass


        # widgets added in order, so mind the order.



class EpicApp(App):
    def build(self):
        return ConnectPage()


if __name__ == "__main__":
    pointeur= data.Text_generator()
    pointeur.init()
    EpicApp().run()
