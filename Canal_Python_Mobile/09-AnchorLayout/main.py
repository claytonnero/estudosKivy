from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Rodando(GridLayout):
	pass

class Roda(App):
	def build(self):
		return Rodando()

if __name__ == '__main__':
	app = Roda()
	app.title = 'Cor De Fundo'
	app.icon = 'icon.png'
	app.run()
