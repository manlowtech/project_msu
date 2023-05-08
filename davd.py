from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp

KV = '''
BoxLayout:
    orientation:"vertical"
    MDTopAppBar:
        left_action_items:[["menu",lambda x:nav.toggle_nav_drawer() ]]
    MDNavigationLayout:
        id:nav
        MDNavigationDrawer:
            Button:
                text:"Screen 1"
                on_release : my_manager.current =  "screen2"
       
        ScreenManager:
            id:my_manager
            Screen:
                name:"screen1"
                MDLabel:
                    text:"Screen One"
                    md_bg_color:"white"
            Screen:
                name:"screen2"
                MDLabel:
                    text:"Screen Two"
                    md_bg_color:"white"
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)


TestNavigationDrawer().run()