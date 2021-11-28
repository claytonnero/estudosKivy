from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.lang import Builder

Builder.load_file('rodar.kv')

class Rodando(StackLayout):
    pass

class Roda(App):
    def build(self):
        return Rodando()

if __name__ == '__main__':
    prog = Roda()
    prog.icon='icon.png'
    prog.title='Classe Rodando 04-rl-tb'
    prog.run()
    
