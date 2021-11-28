from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, ListProperty
from kivy.animation import Animation
from random import random

class Manager(ScreenManager):
    pass

class Menu(Screen):
    pass

class Game(Screen):
    obstacles = []
    #o método on_enter é para quando entrarmos na tela de jogo 
    def on_enter(self, *args):
        # para isso precisamos chamar um método que fica atualizando a 
        #posição do player 30 vezes por segundo
        #para isso precisamos agendar um intervalo de execução com o (Clock)
        Clock.schedule_interval(self.update, 1/30)
        Clock.schedule_interval(self.putObstacle,1)

    def on_pre_enter(self, *args):
        self.ids.player.y = self.height/2
        self.ids.player.speed = 0

   #o método update é o que vai atualizar a tela com o player    
    def update(self, *args):

        #self.ids.player.speed += -500 * 1/30

        # aqui abaixo estamos usando uma fração da tela no caso self.height 
        #é o tamanho da tela e vc multiplica pela fração da tela no caso 0.5
        # ou apenas o self.height
        self.ids.player.speed += -self.height*2 * 1/30
        self.ids.player.y += self.ids.player.speed * 1/30
        if self.ids.player.y > self.height or self.ids.player.y < 0:
            self.gameOver()

    def putObstacle(self, *args):
        gap = self.height*0.3
        position = (self.height-gap)* random()
        width = self.width*0.05
        obstaclelow = Obstacle(x=self.width, height=position, width=width)
        obstaclehigth = Obstacle(x=self.width, y=position+gap, height=self.height-position-gap, width=width)
        obstacle = Obstacle(x=self.width, height=400)
        self.add_widget(obstaclelow)
        self.add_widget(obstaclehigth)
        self.obstacles.append(obstaclelow)
        self.obstacles.append(obstaclehigth)

    def gameOver(self, *args):
        Clock.unschedule(self.update, 1/30)
        Clock.unschedule(self.putObstacle,1)
        for ob in self.obstacles:
            ob.anim.cancel(ob)
            self.remove_widget(ob)
        self.obstacles = []
        #Vamos trocar a tela 
        App.get_running_app().root.current = 'gameOver'

    #Este método on_touch_down será chamado quando tocarmos a tela ou 
    # quando clicarmos com o mouse
    def on_touch_down(self, *args):

        #Aqui multiplicamos a velocidade do player por uma fração positiva
        # da tela para o player pular quando a tela for tocada ou clicada
        self.ids.player.speed = self.height*0.7

class Obstacle(Widget):

    color = ListProperty([0.3,0.2,0.2,1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anim = Animation(x=-self.width, duration=3)
        self.anim.bind(on_complete=self.vanish)
        self.anim.start(self)

    def vanish(self, *args):
        #if self.parent:
        #    self.parent.remove_widget(self)
        gameScreen = App.get_running_app().root.get_screen('game')
        gameScreen.remove_widget(self)
        gameScreen.obstacles.remove(self)



class GameOver(Screen):
    pass

class Player(Image):

    speed = NumericProperty(0)

class Roda(App):
    pass

Roda().run()
