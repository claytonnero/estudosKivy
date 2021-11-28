from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

class Roda(App):
	def build(self):
		player = Image(source='../dados/player.png')
		layout = FloatLayout()
		layout.add_widget(player)
		return layout

Roda().run()
