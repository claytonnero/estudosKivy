from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Rodando(BoxLayout):
	font = "/storage/emulated/0/Hebraico/fonts/cousine/Cousine-Regular.ttf"
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		imp = self.ids.imp
		#imp.text_language = "he"
		
		
	
class Roda(App):
	def build(self):
		return Rodando()

Roda().run()