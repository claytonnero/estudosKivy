from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast.kivytoast.kivytoast import toast

kv = """
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        id: toolbar
        title: app.title
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [["menu", lambda x: None]]

    FloatLayout:

        MDRaisedButton:
            text: "TEST KIVY TOAST"
            on_release: app.show_toast()
            pos_hint: {"center_x": .5, "center_y": .5}

"""


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "KivyMD Examples - Toast"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(kv)

    def show_toast(self):
        #toast("Test Kivy Toast")
        toast("Test Kivy Toast", duration=3)  # toast with user duration


if __name__ == "__main__":
    MainApp().run()