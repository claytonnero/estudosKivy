from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.image import CoreImage
from kivy.lang import Builder

from PIL import Image

kv = Builder.load_string('''
#:kivy 1.11.0

<RootWidget>:
    img: img
    do_default_tab: False

    TabbedPanelItem:
        text: 'PIL Image'

        Screen:
            BoxLayout:
                orientation:"vertical"
                Label:
                    text:str(img.size)
                Image:
                    id: img
                    size_hint: 1, 1
                    allow_stretch: True
''')


class RootWidget(TabbedPanel):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        iw = Image.open("alana.jpg").rotate(-90)
        size = 1280, 780
        iw.thumbnail(size, Image.ANTIALIAS)
        
        iw.save('temp/phase.jpg')
        texto = str(iw.size)
        
        p_e_b = iw.convert('1')
        
        p_e_b.save('temp/gray_im.jpg')
        
        self.img.source = "temp/phase.jpg"

class KivyPILApp(App):
    title = "Kivy & PIL Demo"

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    KivyPILApp().run()