from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

kv = """
MDFloatLayout:
    MDToolbar:
        pos_hint:{"center_y":.97}
        
    MDLabel:
        text:'Olhe aqui o kivymd em execução'
        color:app.theme_cls.primary_color
        halign:'center'
    MDRaisedButton:
        widget_style:"ios"
        text:'button kivymd'
        pos_hint:{"center_x": .5, "center_y": .4}
        text_color:app.theme_cls.primary_light
    

"""

class Roda(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        with open("theme_cls.txt", "w") as arq:
            for i in dir(self.theme_cls):
                if i != "__":
                    print(i, file=arq)
        return Builder.load_string(kv)
        
Roda().run()
