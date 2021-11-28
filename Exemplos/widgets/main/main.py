from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

kv = '''
<Procura>:
	BoxLayout:
		orientation:"vertical"
		size:root.width, root.height
		padding:50
		spacing:20
'''
Builder.load_string(kv)

class Procura(Widget):
	pass

class Roda(App):
	def build(self):
		return Procura()

Roda().run()