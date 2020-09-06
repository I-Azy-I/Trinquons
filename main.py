import data
import text_editor
import kivy

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.picker import MDDatePicker

kivy.require("1.11.1")
KV = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineAvatarListItem:
                text: "Date"
                on_press:
                    app.tap_date()

                IconLeftWidget:
                    icon: "calendar"
                    on_press:
                        app.tap_date()



            OneLineAvatarListItem:
                text: "Tag"
                on_press:
                    root.nav_drawer.set_state("close")
                IconLeftWidget:
                    icon: "tag"
                    on_press:
                        root.nav_drawer.set_state("close")


Screen:

    MDFloatingActionButton:
        id: menu
        icon: "menu"

        pos: 10,self.parent.top - 50
        on_release: app.tap_menu()



    MDFloatingActionButton:
        id: refresh
        icon: "refresh"

        pos: 10,10
        on_release: app.tap_refresh()

    NavigationLayout:


        ScreenManager:
            id: screen_manager

            Screen:
                name: "scr 1"

                MDLabel:
                    id: label1
                    text: "Screen 1"
                    halign: "center"

            Screen:
                name: "scr 2"

                MDLabel:
                    id: label2
                    text: "Screen 2"
                    halign: "center"
            Screen:
                name : "tag"


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        self.date_choose=""
        self.screen=1
        self.screen = Builder.load_string(KV)
        self.tap_refresh()
        return self.screen

    def tap_refresh(self):
        if self.date_choose=="":
            data=pointeur.get_text()
        else:
            data=pointeur.get_text(self.date_choose)
        text=data[1]
        tag=data[0]
        try :
            message=text_editor.text_affiche(tag,text)
        except:
            pass
        if self.screen.ids.screen_manager.current == "scr 1":
            self.screen.ids.screen_manager.current ="scr 2"
            self.screen.ids.label2.text=message
        else:
            self.screen.ids.screen_manager.current ="scr 1"
            self.screen.ids.label1.text=message

    def tap_menu(self):
        self.screen.ids.nav_drawer.set_state("open")

    def get_date(self, date):
        self.date_choose=date.strftime("%d.%m")
        self.screen.ids.nav_drawer.set_state("close")
        self.tap_refresh()

    def tap_date(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

if __name__ == "__main__":
    pointeur= data.Text_generator()
    pointeur.init()
    TestNavigationDrawer().run()
