#encoding:utf-8

# importando nossa aplicação, esta será a classe mais importante em nosso programa
from kivy.app import App

# importando nosso layout, neste caso o BoxLayout
from kivy.uix.boxlayout import BoxLayout 

# importando o botão a ser usado 
from kivy.uix.button import Button

class Tarefas(BoxLayout):
	"""
	A classe Tarefas cria os widgets de forma dinâmica, de uma lista de tarefas
	que pode ser acrescentado dinamicamente
	"""
	def __init__(self, Tarefas, **kwargs): # **kwargs
		"""
		__init__ é a função que inicia a classe, todos os comandos subordinados a ele
		será executado na inicialização da classe!
		"""
		# o super é chamado para rodar o metodo __init__ do BoxLayout
		# caso não o faça o método __init__ criado por vc subscreva o init da classe principal		
		super().__init__(**kwargs)

		for tarefa in Tarefas:
			"""
			Aqui uma iteração de tarefa na lista passada como argumento na chamada 
			do programa neste caso Tarefas, portanto tarefa percorrerá toda lista
			e acrecentará um widget para cada item na lista Tarefas
			"""
			#criando o botão com o texto do item da lista Tarefas atribuido à tarefa
			self.but = Button(text=tarefa, on_release=self.click)
			
			# este comando adiciona o widget em nossa janela
			self.add_widget(self.but)
	
	def click(self, but):
		"""
		click é executada quando o botão for pressionado dentro de tarefas
		"""		
		print("Apertado")
		
class Roda(App):
	"""
	Esta classe foi criada no curso, ela integra todas as funcionalidades
	presentes na classe App importada e passada como parametro nessa função
	"""
	def build(self):
		"""
		Este método build serve para construir nossa janela, e é padrão do kivy
		tudo dentro desta função será executado quando a classe Ola for chamada 
		como na última linha dese programa!
		"""	
		# Aqui a função build retorna a classe que criamos acima Pega_kv, com uma lista como argumento	
		return Tarefas(["testando", "testado", "pra testar", "bola", "games", "estudar"], orientation='horizontal') #a opção orientation usada aqui como parametro para classe Tarefas
		#só é possiver se **kwargs for colocada como argumento na definição do método __init__ (self, Tarefas, **kwargs)da classe Tarefas e também no super super().__init__(**kwargs)

###################################################
#######encerrando as declarações###################
###################################################


###################################################
############## Rodando a Aplicação ################
###################################################

Roda.title = "Layouts Dinamicos e Kwarg" # isto muda o nome da janela
Roda.icon = "../dados/imagens/icon.png"

Roda().run()
# Aqui o programa é realmente executado nossa classe Ola() 
# que por sua vez herda da classe App, e chama uma função
# da propria App que é o método run(), este realmente dispara a app!!

################################################### 
################ Fim a Aplicação ##################
################################################### 
