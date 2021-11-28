from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class Rodando(AnchorLayout):
	def __init__(self, **kwargs):
		super(Rodando, self).__init__(**kwargs)
		self.anchor_x = "center"
		self.anchor_y = "top"
		btn1 = Button(text='Hello', size_hint=(.5, .3))
		btn2 = Button(text='World', size_hint=(.2, .7))
		self.add_widget(btn1)
		self.add_widget(btn2)

class Roda(App):
	def build(self):
		return Rodando()

Roda().run()