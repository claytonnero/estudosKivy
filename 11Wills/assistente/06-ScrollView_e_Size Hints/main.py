#encoding:utf-8

#encoding:utf-8

# importando nossa aplicação, esta será a classe mais importante em nosso programa
from kivy.app import App

# importando nosso layout, neste caso o BoxLayout
from kivy.uix.boxlayout import BoxLayout 

# importando o botão a ser usado 
from kivy.uix.button import Button

# importando o botão a ser usado 
from kivy.uix.label import Label

# importando a janela de rolagem ScrollView
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
	"""
	A classe Tarefas cria os widgets de forma dinâmica, de uma lista de tarefas
	que pode ser acrescentado dinamicamente
	"""	
	def __init__(self, Tarefas, **kwargs):
		"""
		__init__ é a função que inicia a classe, todos os comandos subordinados a ele
		será executado na inicialização da classe!
		"""

		# o super é chamado para rodar o metodo __init__ do BoxLayout
		# caso não o faça o método __init__ criado por vc subscreva o init da classe principal
		super().__init__(**kwargs)

		for self.tarefa in Tarefas:
			"""
			Aqui uma iteração de tarefa na lista passada como argumento na chamada 
			do programa neste caso Tarefas, portanto tarefa percorrerá toda lista
			e acrecentará um widget para cada item na lista Tarefas
			"""
			#criando o Label com o texto do item da lista Tarefas atribuido à tarefa
			self.lab = Button(text=self.tarefa, font_size=20, size_hint_y=None, height=80, on_press=self.aperta)

			# este comando adiciona o widget em nossa janela
			self.ids.box.add_widget(self.lab)	
	
	def aperta(self, lab):
		print(dir(App))
		
class Roda(App):
	def build(self):
			
		return Tarefas(dir(App))

###################################################
#######encerrando as declarações###################
###################################################


###################################################
############## Rodando a Aplicação ################
###################################################

Roda.title = "Scrollview e Size_hints" # isto muda o nome da janela
Roda.icon = "../dados/imagens/icon.png"

Roda().run()
# Aqui o programa é realmente executado nossa classe Ola() 
# que por sua vez herda da classe App, e chama uma função
# da propria App que é o método run(), este realmente dispara a app!!

################################################### 
################ Fim a Aplicação ##################
################################################### 
