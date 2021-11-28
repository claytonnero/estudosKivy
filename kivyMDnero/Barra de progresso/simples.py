from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
BoxLayout:
    padding: "10dp"

    MDProgressBar:
        color: app.theme_cls.primary_color
        value: 50
        
    MDProgressBar:
        color: app.theme_cls.accent_color
        orientation:"vertical"
        value: 80
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()