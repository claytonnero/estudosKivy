#encoding:utf-8

#importando nossa aplicação, esta será a classe mais importante em nosso programa
from kivy.app import App

#importando nosso widget, neste caso o Button, serve de botão para clicarmos e eles farão o que determinarmos em nosso programa
from kivy.uix.button import Button

#BoxLayout importando nosso layout, neste caso o BoxLayout
from kivy.uix.boxlayout import BoxLayout 

#importando nosso widget, neste caso o Label, serve para colocar textos em nosso programa
from kivy.uix.label import Label 

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
		# passo muito importante, a variável box recebe o Boxlayout, percebe e o BoxLayout está cendo chamado com (), isso significa que ela foi instanciada, e atribuida a box!!!
		caixa = BoxLayout(orientation='vertical') #Boxlayout tem diversos parametros, orientation define a orientação!

		#Este é um widget chamado Button que como o nome diz é um botão e tem várias funções internas, foi atribuido a variável botao!
		botao = Button(text="Botão 1 box!")

		#Já este, é um widget chamado Label que é utilizado para colocar textos em nosso programa, e o Label foi atribuido a variável texto com o parametro(text='textos') 
		texto = Label(text="Olha eu dentro do box!")
		
		# Aqui sim o botão está sendo colocado dentro do BoxLayout, com a opção add_widget(botão), que é um método do Boxlayout!
		caixa.add_widget(botao)

		# Aqui sim o botão está sendo colocado dentro do BoxLayout, com a opção add_widget(texto), que é um método do Boxlayout!
		caixa.add_widget(texto)

		# e podemos colocar um layout dentro do outro
		caixa1 = BoxLayout() # esta é uma nova chamada do boxlayout
		#Boxlayout tem diversos parametros, orientation define a orientação, neste caso  BoxLayout() sem parametro nenhum tem por padrão orientação horizontal!

		# Aqui definimos vários botões e um label como feito antes, só que com outros nomes!
		botao1 = Button(text="Botão 1 box1!")
		botao2 = Button(text="Botão 2 box1!")
		botao3 = Button(text="Botão 3 box1!")
		botao4 = Button(text="Botão 4 box1!")
		texto1 = Label(text="Olha eu dentro do box=1!")	

		# para funcionar vc deve adicionar os widgets declarados, caso contrário, seu programa não mostrará os widgets 	
		caixa1.add_widget(botao1)
		caixa1.add_widget(botao2)
		caixa1.add_widget(texto1)
		caixa1.add_widget(botao3)
		caixa1.add_widget(botao4)
		
		# Aqui vc deve adicionar o box1 ao box!
		caixa.add_widget(caixa1)
		# E retornamos da função build o box!!
		return(caixa)

###################################################
#######encerrando as declarações###################
###################################################


###################################################
############## Rodando a Aplicação ################
###################################################

Roda.title = "Clayton" # isto muda o nome da janela
Roda.icon = "../dados/imagens/icon.png"

Roda().run()
# Aqui o programa é realmente executado nossa classe Ola() 
# que por sua vez herda da classe App, e chama uma função
# da propria App que é o método run(), este realmente dispara a app!!

################################################### 
################ Fim a Aplicação ##################
################################################### 
