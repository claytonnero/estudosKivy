from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import math

class Rodando(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.lab.text = "alterado"
        
        if self.ids.text.focus == True:
            self.ids.text.text._deleteline()
        
        
    def processado(self, Button):
        if self.ids.text.text == "":
            self.ids.lab.text = "Digite alguma coisa na\n entrada de texto"
        else:
            try:
                self.ids.lab.text = "O perímetro do \nraio solicitado é "+str(int((2*math.pi)*float(self.ids.text.text)))
                Button.background_color = 0,1,1,1
            except ValueError:
                self.ids.lab.text="Use somente números reais!"
                 
class Roda(App):
    def build(self):
        return Rodando()
        
Roda().run()       