#! /usr/bin/env python3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
	pass

class Fazendo(Screen):
	
	def __init__(self, Tarefas=[], **kwargs):
                
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
		return Gerenciador()

Roda.title='Múltiplas Telas com ScreenManager'
Roda.icon="../dados/imagens/icon.png"

Roda().run()
 
