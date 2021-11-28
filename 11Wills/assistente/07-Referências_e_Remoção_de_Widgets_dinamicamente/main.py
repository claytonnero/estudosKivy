#encoding:utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
	
	def __init__(self, Tarefas, **kwargs):
		super().__init__(**kwargs)
		for tarefa in Tarefas:			
			self.ids.box.add_widget(Tarefa(text=tarefa))	

class Tarefa(BoxLayout):

	def __init__(self, text="", **kwargs):
		super().__init__(**kwargs)
		self.ids.label.text = text
		
class Roda(App):
	def build(self):
			
		return Tarefas(dir(App)) #["testando", "testado", "pra testar", "bola", "games", "estudar", "Brincar", "dormir"]

###################################################
#######encerrando as declarações###################
###################################################


###################################################
############## Rodando a Aplicação ################
###################################################

Roda.title = "Referências e Remoção de Widgets Dinamicamente" # isto muda o nome da janela
Roda.icon = "../dados/imagens/icon.png"

Roda().run()
# Aqui o programa é realmente executado nossa classe Ola() 
# que por sua vez herda da classe App, e chama uma função
# da propria App que é o método run(), este realmente dispara a app!!

################################################### 
################ Fim a Aplicação ##################
################################################### 
