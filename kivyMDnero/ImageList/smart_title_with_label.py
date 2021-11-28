from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
<MyTile@SmartTileWithLabel>
    size_hint_y: None
    height: "240dp"


ScrollView:

    MDGridLayout:
        cols: 3
        adaptive_height: True
        padding: dp(4), dp(4)
        spacing: dp(4)

        MyTile:
            source: "juju.jpg"
            text: "O garoto juju"

        MyTile:
            source: "juju1.jpg"
            text: "Juju o bb do vô"
            tile_text_color: app.theme_cls.accent_color

        MyTile:
            source: "juju2.jpg"
            text: "Veja como ele é forte"
            tile_text_color: app.theme_cls.accent_color
'''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MyApp().run()