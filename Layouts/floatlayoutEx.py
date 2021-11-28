from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

kv = """
<Rodando>:
	Button:
		text:"Texto"
		size_hint:(.5, .25)
		pos:(20,20)
	Button:
		text:"botao"
		size_hint:(.3, .6)
		pos_hint:({"x":.2, "center_y":1})

"""

class Rodando(FloatLayout):
	Builder.load_string(kv)
	def __init__(self, **kwargs):
		super().__init__(**kwargs)		

class Roda(App):
	def build(self):
		return Rodando()

Roda().run()