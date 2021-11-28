from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.toast import toast

kv = """
BoxLayout:
    orientation: "vertical"
    spacing: dp(10)

    MDToolbar:
        title: app.title
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [["menu", lambda x: x]]
        background_palette: "Primary"

    ScrollView:

        GridLayout:
            padding: dp(10)
            spacing: dp(10)
            cols: 1
            size_hint_y: None
            height: self.minimum_height

            MDLabel:
                text: "Chips with color:"

            MDSeparator:

            StackLayout:
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(5)

                MDChip:
                    label: "Coffee"
                    color: .4470588235294118, .19607843137254902, 0, 1
                    icon: "coffee"
                    callback: app.callback

                MDChip:
                    label: "Duck"
                    color: .9215686274509803, 0, 0, 1
                    icon: "duck"
                    callback: app.callback

                MDChip:
                    label: "Earth"
                    color: .21176470588235294, .09803921568627451, 1, 1
                    icon: "earth"
                    callback: app.callback

                MDChip:
                    label: "Face"
                    color: .20392156865098, .48235294117606, .43529411764705883, 1
                    icon: "face"
                    callback: app.callback

                MDChip:
                    label: "Facebook"
                    color: .5607843137254902, .48235294164706, .435294117705883, 1
                    icon: "facebook"
                    callback: app.callback

            Widget:
                size_hint_y: None
                height: dp(5)

            MDLabel:
                text: "Chip without icon:"

            MDSeparator:

            StackLayout:
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(5)

                MDChip:
                    label: "Without icon"
                    icon: ""
                    callback: app.callback

            Widget:
                size_hint_y: None
                height: dp(5)

            MDLabel:
                text: "Chips with check:"

            MDSeparator:

            StackLayout:
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(5)

                MDChip:
                    label: "Check"
                    icon: ""
                    check: True
                    callback: app.callback

                MDChip:
                    label: "Check with icon"
                    icon: "city"
                    check: True
                    callback: app.callback
            Widget:
                size_hint_y: None
                height: dp(5)

            MDLabel:
                text: "Choose chip:"

            MDSeparator:

            MDChooseChip:

                MDChip:
                    label: "Earth"
                    icon: "earth"
                    callback: app.callback
                    selected_chip_color: .21176470535294, .098039627451, 1, 1

                MDChip:
                    label: "Face"
                    icon: "face"
                    callback: app.callback
                    selected_chip_color: .21176470535294, .098039627451, 1, 1

                MDChip:
                    label: "Facebook"
                    icon: "facebook"
                    callback: app.callback
                    selected_chip_color: .21176470535294, .098039627451, 1, 1
"""


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "KivyMD Examples - Chip"
        self.theme_cls.primary_palette = "Red"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(kv)

    def callback(self, instance, value):
        toast(value)


if __name__ == "__main__":
    MainApp().run()