#encoding:utf-8

#importando nossa aplicação, esta será a classe mais importante em nosso programa
from kivy.app import App

#importando nosso layout, neste caso o BoxLayout
from kivy.uix.boxlayout import BoxLayout 

class Pega_kv(BoxLayout):
	"""
	Esta classe foi criada no curso, ela integra todas as funcionalidades
	presentes na classe BoxLayout importada e será incrementada no arquivo .kv
	o arquivo .kv deve ter o mesmo nome que a classe principal do programa 
	neste caso roda.kv e obrigatóriamente deve ter o nome em minúsculo, caso contrario
	o kivy não vai reconhecê-lo por este método!
	"""
	pass

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
		# Aqui a função build retorna a classe que criamos acima Pega_kv	
		return Pega_kv()

###################################################
#######encerrando as declarações###################
###################################################


###################################################
############## Rodando a Aplicação ################
###################################################

Roda.title = "Janela Com Linguagem Kv " # isto muda o nome da janela
Roda.icon = "../dados/imagens/icon.png"

Roda().run()
# Aqui o programa é realmente executado nossa classe Ola() 
# que por sua vez herda da classe App, e chama uma função
# da propria App que é o método run(), este realmente dispara a app!!

################################################### 
################ Fim a Aplicação ##################
################################################### 
