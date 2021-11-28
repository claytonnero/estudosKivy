from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.label import Label

som = SoundLoader.load("/storage/emulated/0/Music/NinguémExplicaDeus.mp3")

class Roda(App):
	
	print(dir(som))
	
	def build(self):
		lab = Label()
		if som:
			som.volume = .6
			stri = f"""
   {som.source}
   Este som ^^^ executando!
   
   {som.events()}
   
   Tamanho
   {som.length}
   
   posição {som.get_pos()}
   
   O volume está {som.volume}"""
			lab.text = "Entrei no if!!"
			print(help(som.get_property_observers))
			som.play()
			lab.text = stri
		return lab
		
Roda().run()