from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class FULLDAYApp(MDApp):
     def build(self):
        return MDLabel(text="Hello, ladies", halign="center")


FULLDAYApp().run()