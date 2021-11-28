from editor import ed
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.clearcolor = .92,  .92, .92, 1

kv = """
#:set cor_texto .57, .57, .57, 1
#:set cor_fundo .92, .92, .92, 1
#:set cor_borda .80, .80, .80, 1
#:set cor_botao .65, .65, .65, 1
#:set cor_botao_azul .23, .41, .78, 1
#:set cor_botao_laranja .93, .52, .31, 1

<TelaInicial@Screen>:
    Boxlayout:
        padding:15
        Image:
            source:"alana.jpg"
"""

class Edit(App):
    title = "Android Editor de imagem"
    def build(self):
        return Builder.load_string(kv)
        
if __name__ == "__main__":
    Edit().run()

