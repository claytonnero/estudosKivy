from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = .92,  .92, .92, 1

kv = """
#:set cor_texto .57, .57, .57, 1
#:set cor_fundo .92, .92, .92, 1
#:set cor_borda .80, .80, .80, 1
#:set cor_botao .65, .65, .65, 1
#:set cor_botao_azul .23, .41, .78, 1
#:set cor_botao_laranja .93, .52, .31, 1

Screen:
    MDBoxLayout:
        padding:15
        MDBoxLayout:
            canvas:
                color:
                    rgba: 1,1,1,1
                Rectangle:
                    size:self.size
                    pos:self.pos
"""

class Edit(MDApp):
    title = "Android Editor de imagem"
    def build(self):
        return Builder.load_string(kv)
        
if __name__ == "__main__":
    Edit().run()