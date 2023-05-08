from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# ============WELCOME NOTES SCREEN=====
class WelcomeNote(Screen):
    """
    THIS FIRST FETCHES FROM SQLITE IF WELCOME NOTES WAS DISPALYED BEFORE
    ELSE DONT SHOW IT
    """
# ===============================REGISTRATION WINDOW========================
class RegisterPage(Screen):
    pass
# =====LOGIN WINDOW=====
class LoginScreen(Screen):
    pass
# ============= DASHBOARD SCREEN =============
"""
BEFORE NAVIGATING TO ANOTHER SCREEN CHECK IF USER IS LOGGED IN OR NOT
"""
class DashboardScreen(Screen):
    pass
class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


#kv = Builder.load_file("inclusiveai.kv")


class MyMainApp(MDApp):
    def build(self):
        #self.root.ids.dash_label.text = "Text Was a Success"
        #self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "Cyan"
        return Builder.load_file("inclusiveai.kv")

"""
from kivy.clock import Clock

Use clock to modify the text in the label to match what was said by the user
"""
if __name__ == "__main__":
    MyMainApp().run()
