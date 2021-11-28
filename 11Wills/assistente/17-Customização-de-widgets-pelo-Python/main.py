#! /usr/bin/env python3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle

class Gerenciador(ScreenManager):
	pass

class Menu(Screen):
	pass
#aula 17 Botoes diamicos com o python
class Botao(ButtonBehavior,Label):
	
	def __init__(self, **kwargs):
		super(Botao,self).__init__(**kwargs)
		self.atualizar()

	def on_pos(self, *args):
		self.atualizar()

	def on_size(self, *args):
		self.atualizar()

	def atualizar(self, *args):	
		self.canvas.before.clear()	
		with self.canvas.before:
			Color(rgba=(0.2,0.5,0.7,1))
			Ellipse(pos=self.pos, size=(self.height,self.height))
			Ellipse(pos=(self.x+self.width-self.height, self.y), size=(self.height,self.height))
			Rectangle(pos=(self.x+self.height/2.0, self.y), size=(self.width-self.height, self.height))

class Fazendo(Screen):
	
	def __init__(self, Tarefas=[], **kwargs):#neste caso trata como dicionario
                
		super().__init__(**kwargs)
		
		for tarefa in Tarefas:                        
			self.ids.box.add_widget(Tarefa(text=tarefa))	
	
	def on_pre_enter(self):
		Window.bind(on_keyboard=self.voltar)

	def voltar(self, window, key, *args):#neste caso trata como lista
		
		if key == 27:		
			App.get_running_app().root.current = 'menu'
			#print(key) #mostra as teclas pressionadas
			return True

	def on_pre_leave(self):	
		Window.unbind(on_keyboard=self.voltar)

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

Roda.title='Customização de Widgets Pelo Python'
Roda.icon='../dados/imagens/icon.png'
Roda().run()
