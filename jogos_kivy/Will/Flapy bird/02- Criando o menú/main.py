from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image

class Manager(ScreenManager):
	pass

class Menu(Screen):
	pass
	
class Game(Screen):
	pass
	
class Player(Image):
	pass

class Roda(App):
	pass

Roda().run()
