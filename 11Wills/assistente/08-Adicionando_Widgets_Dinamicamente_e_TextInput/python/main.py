#! /usr/bin/env python3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder

#este recurso permite integrar o arquivo.kv dentro do seu script
Builder.load_string("""
<Tarefas>:
	orientation:'vertical'
	ScrollView:
		BoxLayout:
			id:box
			orientation:'vertical'
			size_hint_y:None
			height:self.minimum_height
	BoxLayout:
		size_hint_y:None
		height:40
		TextInput:
			id:texto
		Button:
			text:'+'
			size_hint_x:None
			width:40
			on_release:root.addWidget()
<Tarefa>:
	size_hint_y:None
	height:200
	Label:
		id:label
		font_size:30
	Button:		
		text:'X'
		size_hint_x:None
		width:40
		on_release:app.root.ids.box.remove_widget(root)
""")

class Tarefas(BoxLayout):
	
	def __init__(self, Tarefas, **kwargs):
                
		super().__init__(**kwargs)
		
		for tarefa in Tarefas:
                        
			self.ids.box.add_widget(Tarefa(text=tarefa))	
	
	def addWidget(self):
                
		texto = self.ids.texto.text
		self.ids.box.add_widget(Tarefa(text=texto))
		self.ids.texto.text = ""

class Tarefa(BoxLayout):

	def __init__(self, text="", **kwargs):
                
		super().__init__(**kwargs)
		self.ids.label.text = text
		
class Roda(App):
	def build(self):
		return Tarefas(["testando", "testado", "pra testar", "bola", "games", "estudar", "Brincar", "dormir"])
Roda.title='Adicionando Widgets'
Roda.icon= '../../dados/imagens/icon.png'
Roda().run()
 
