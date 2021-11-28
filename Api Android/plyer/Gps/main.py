from kivy.app import App
from plyer import gps

class Roda(App):
	lista = []
	for i in dir(gps):
		lista.append(i)
#1220
Roda().run()