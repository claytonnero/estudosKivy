from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from plyer.facades import Flash

class Rodando(BoxLayout):
    
    def solto(self, botao):
        Flash.on(self)

class Roda(App):
    def build(self):
        return Rodando()
        
Roda().run()
