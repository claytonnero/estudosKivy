# pong game
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.clock import Clock
from kivy.vector import Vector

class Rodando(Widget):
	bola = ObjectProperty(None)
	
	def update(self, dt):
		self.bola.move()
		
		if (self.bola.y < 0) or (self.bola.top > self.height):
			self.bola.velocidade_y *= -1
		if (self.bola.x < 0) or (self.bola.right > self.width):
			self.bola.velocidade_x *= -1
				

class PongBall(Widget):
	
	velocidade_x = NumericProperty(0)
	velocidade_y = NumericProperty(0)
	velocidade = ReferenceListProperty(velocidade_x, velocidade_y)
	
	def move(self):
		self.pos = Vector(*self.velocidade) + self.pos

class Roda(App):
	def build(self):
		jogo = Rodando()
		Clock.schedule_interval(jogo.update, 1.0/60.0)
		return jogo

Roda().run()