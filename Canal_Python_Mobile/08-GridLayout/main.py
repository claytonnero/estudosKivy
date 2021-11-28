import kivy.uix.gridlayout as TheGrid
from kivy.app import App

class Rodando(TheGrid.GridLayout):
    pass

class Roda(App):
    def build(self):
        return Rodando()

if __name__ == "__main__":
    prog = Roda()
    prog.icon = 'icon.png'
    prog.title = '07-GridLayout'
    prog.run()
