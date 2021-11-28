#encoding:utf-8

#esta é a classe principal da qual herdara nossa aplicação
from kivy.app import App 

#Este é um widget chamado Button que como o nome diz é um botão e tem várias funções internas!
from kivy.uix.button import Button 

# Assim funciona nosso programa, a janela em sí, 'classe App'!
# incrementado com os chamados 'widgets', basicamente os programas funcionam assim mesmo

class Ola(App):
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
		# nesta linha a função build retorna o que for processado dentro da função build!
		return(Button(text="Olá mundão de meu Deus!", font_size=50, )) 

###################################################
#######encerrando as declarações###################
###################################################


###################################################
############## Rodando a Aplicação ################
###################################################

Ola.title = "Olá Mundo Aula 1" # isto muda o nome da janela
Ola.icon = "../dados/imagens/icon.png"

Ola().run()
# Aqui o programa é realmente executado nossa classe Ola() 
# que por sua vez herda da classe App, e chama uma função
# da propria App que é o método run(), este realmente dispara a app!!

################################################### 
################ Fim a Aplicação ##################
################################################### 
