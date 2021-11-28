from kivymd.app import MDApp
from kivy.lang import Builder

kv = """
MDLabel:
	text:"deu certo"
"""

class Roda(MDApp):
	def build(self):
		return Builder.load_string(kv)
				
Roda().run()