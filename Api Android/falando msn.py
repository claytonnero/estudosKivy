from kivy.app import App
from plyer import tts, stt
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget 

class Cena(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.ent = TextInput(hint_text="escreva a frase a ser falada", multiline=False, size_hint_y=None, height="40dp")
        but = Button(text="Fala Garota", on_release=self.solto)      
        self.add_widget(self.ent)
        self.add_widget(Widget())
        self.add_widget(but)
    
    def solto(self, botao):
        ent = self.ent.text
        tts.speak(ent)
        print(help(tts.speak))
        
class Apresenta(App):
    def build(self):
        return Cena() 
Apresenta().run()