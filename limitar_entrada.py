from kivy.app import App
from kivy.base import Builder
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


Builder.load_string("""
<BoundedLayout>:
    orientation: 'horizontal'
    Label:
        text: 'Value'
    NumericInput:
        min_value : 5
        max_value : 100
        hint_text : 'Enter values between {} and {}'.format(self.min_value, self.max_value)
""")

class NumericInput(TextInput):
    min_value = NumericProperty()
    max_value = NumericProperty()
    def __init__(self, *args, **kwargs):
        TextInput.__init__(self, *args, **kwargs)
        self.input_filter = 'float'
        self.multiline = False

    def insert_text(self, string, from_undo=False):
        new_text = self.text + string
        if new_text != "":
            if self.min_value <= float(new_text) <= self.max_value:
                TextInput.insert_text(self, string, from_undo=from_undo)

class BoundedLayout(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return BoundedLayout()

if __name__ == '__main__':
    MyApp().run()