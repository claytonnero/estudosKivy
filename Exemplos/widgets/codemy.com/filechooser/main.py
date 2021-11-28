from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

kv = '''
<Procura>:
	id:todo
	BoxLayout:
		orientation:"vertical"
		size:root.width, root.height
		padding:50
		spacing:20
		
		Image:
			id:imagem
			source:" "
			
		FileChooserIconView:
			id:procura
			on_selection:todo.selecionado(procura.selection)
'''
Builder.load_string(kv)

class Procura(Widget):
	def selecionado(self, filename):
		try:
			self.ids.imagem.source = filename[0]		
		except:
			pass

class Roda(App):
	def build(self):
		return Procura()

Roda().run()