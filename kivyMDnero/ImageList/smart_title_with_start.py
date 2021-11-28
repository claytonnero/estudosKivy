from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
<MyTile@SmartTileWithStar>
    size_hint_y: None
    height: "240dp"


ScrollView:

    MDGridLayout:
        cols: 3
        adaptive_height: True
        padding: dp(4), dp(4)
        spacing: dp(4)

        MyTile:
            stars: 5
            source: "juju.jpg"

        MyTile:
            stars: 5
            source: "juju1.jpg"

        MyTile:
            stars: 5
            source: "juju2.jpg"
'''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MyApp().run()