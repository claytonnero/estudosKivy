# Aula 05 BoxLayout
# aqui um novo detalhe, uma novidade na importação de arquivos .kv

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder # Módulo responsável pelo carregamento do arquivo kv
from kivy.app import App

Builder.load_file('olamundo_5.kv')

class MinhaCaixa(BoxLayout):
    pass

class Roda(App):
    def build(self):
        return MinhaCaixa()

if __name__ == '__main__':
    Roda().run()

