from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import NumericProperty

class Manager(ScreenManager):
	pass

class Menu(Screen):
	pass
	
class Game(Screen):
   #o método on_enter é para quando entrarmos na tela de jogo 
    def on_enter(self, *args):
        # para isso precisamos chamar um método que fica atualizando a 
        #posição do player 30 vezes por segundo
        #para isso precisamos agendar um intervalo de execução com o (Clock)
        Clock.schedule_interval(self.update, 1/30)

   #o método update é o que vai atualizar a tela com o player    
    def update(self, *args):

        #self.ids.player.speed += -500 * 1/30

        # aqui abaixo estamos usando uma fração da tela no caso self.height 
        #é o tamanho da tela e vc multiplica pela fração da tela no caso 0.5
        # ou apenas o self.height
        self.ids.player.speed += -self.height * 1/30
        self.ids.player.y += self.ids.player.speed * 1/30

    #Este método on_touch_down será chamado quando tocarmos a tela ou 
    # quando clicarmos com o mouse
    def on_touch_down(self, *args):

        #Aqui multiplicamos a velocidade do player por uma fração positiva
        # da tela para o player pular quando a tela for tocada ou clicada
        self.ids.player.speed = self.height*0.7
	
class Player(Image):
	
    speed = NumericProperty(0)

class Roda(App):
	pass

Roda().run()
