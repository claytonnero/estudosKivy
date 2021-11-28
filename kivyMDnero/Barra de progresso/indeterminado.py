from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp

KV = '''
Screen:

    MDProgressBar:
        id: progress
        pos_hint: {"center_y": .6}
        type: "indeterminate"

    MDRaisedButton:
        text: "STOP" if app.state == "start" else "START"
        pos_hint: {"center_x": .5, "center_y": .45}
'''


class Test(MDApp):
    state = StringProperty("stop")

    def build(self):
        return Builder.load_string(KV)

Test().run()