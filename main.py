import data
import text_editor
import kivy
import webbrowser
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.picker import MDDatePicker
from kivymd.toast import toast

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
                    app.tap_tag()
                IconLeftWidget:
                    icon: "tag"
                    on_press:
                        root.nav_drawer.set_state("close")
                        app.tap_tag()

            OneLineAvatarListItem:
                text: "Instagram"
                on_press:
                    app.tap_insta()
                IconLeftWidget:
                    icon: "instagram"
                    on_press:
                        app.tap_insta()


Screen:



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

                ScrollView:

                    GridLayout:
                        padding: dp(60), dp(100)
                        spacing: dp(10)
                        cols: 1
                        size_hint_y: None
                        height: self.minimum_height




                        StackLayout:
                            pos_hint: {'center_x': 0.7, 'center_y': 0.5}

                            spacing: dp(5)
                            padding: dp(10)
                            size_hint_y: None
                            height: self.minimum_height

                            MDChip:
                                label: "Journées internaionales"
                                icon: "earth"
                                check: True
                                callback: app.tap_chip
                                color:0.8, 0, 0, 1


                            MDChip:
                                label: "Fêtes nationales"
                                icon: "flag-variant"
                                check: True
                                callback: app.tap_chip
                                color:0.8, 0, 0, 1

                            MDChip:
                                label: "Histoire"
                                icon: "book-open-variant"
                                check: True
                                callback: app.tap_chip
                                color:0.8, 0, 0, 1

                            MDChip:
                                label: "Royauté"
                                icon: "castle"
                                check: True
                                callback: app.tap_chip
                                color:0.8, 0, 0, 1




    MDFloatingActionButton:
        id: menu
        icon: "menu"

        pos: 10,self.parent.top - 165
        on_release: app.tap_menu()



    MDFloatingActionButton:
        id: refresh
        icon: "refresh"

        pos: 10,10
        on_release: app.display_event()

    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            screen_manager: screen_manager
            nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TrinquonsApp(MDApp):
    def build(self):
        self.date_choose=""
        self.screen=1
        self.screen = Builder.load_string(KV)
        self.display_event()
        return self.screen

    def display_event(self):
        #obtenir phrase
        data=pointeur.get_text()
        text=data[1]
        tag=data[0]

        try :
            #essaye d'ajouter au label
            message=text_editor.text_affiche(tag,text)
        except:
            message="erreur 128292"
        #affiche sur un des 2 écrans
        if self.screen.ids.screen_manager.current == "scr 1":
            self.screen.ids.screen_manager.current ="scr 2"
            self.screen.ids.label2.text=message
        else:
            self.screen.ids.screen_manager.current ="scr 1"
            self.screen.ids.label1.text=message

    def tap_menu(self):
        self.screen.ids.nav_drawer.set_state("open")

    def get_date(self, date):
        pointeur.today=date.strftime("%d.%m")
        self.screen.ids.nav_drawer.set_state("close")
        pointeur.update()
        self.display_event()

    def tap_date(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()
    def tap_insta(self):
        webbrowser.open('https://www.instagram.com/drink_for_nations/')
    def tap_tag(self):
        self.screen.ids.screen_manager.current = "tag"
    def tap_chip(self,instance, value):

        if instance.color==[0.8, 0, 0, 1]:
            instance.color=0, 0.8, 0, 1
        else:
            instance.color=0.8, 0, 0, 1


        value={
        "Journées internaionales":"journee",
        "Fêtes nationales":"fetes_nationales",
        "Histoire":"histoire",
        "Royauté":"royaute"
        }[value]

        if value in pointeur.tag_blacklist:
            pointeur.tag_blacklist.remove(value)
        else:
            pointeur.tag_blacklist.append(value)
        pointeur.update()


if __name__ == "__main__":
    pointeur = data.Text_generator()
    pointeur.init()
    pointeur.update()
    TrinquonsApp().run()
