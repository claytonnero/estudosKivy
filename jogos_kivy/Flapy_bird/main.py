from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.properties import NumericProperty

class Gerenciador(ScreenManager):
    pass
    
class Jogo(Screen):
    def on_enter(self, *args):
        Clock.schedule_interval(self.atualiza, 1/30)
        
    def atualiza(self, *args):
        self.ids.player.vel += -400 * 1/30
        self.ids.player.y = self.ids.player.vel * 1/30
        
class Passaro(Image):
    vel = NumericProperty(0)
          
class Menu(Screen):
    pass
    
class Roda(App):
    pass

Roda().run()