from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles


KV = '''
Screen:

    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "MDLabel"

        ScrollView:

            MDList:
                id: box
'''


class Test(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        # Names of standard font styles.
        for name_style in theme_font_styles[:-1]:
            screen.ids.box.add_widget(
                MDLabel(
                    text=f"{name_style} style",
                    halign="center",
                    font_style=name_style,
                    size_hint_y = None,
                    height=150
                )
            )
        return screen


Test().run()