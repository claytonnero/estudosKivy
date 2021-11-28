#encoding:utf-8

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Roda(App):
	def build(self):
		box = BoxLayout(orientation="vertical")
		# box recebe BoxLayout com o parâmetro orientação='vertical', isto em python é um dicionário
		# Assim como outros parametros como os abaixo, text, font_size, on_release, todos estes são dicionários em python 
		
		botao = Button(text="Botão 1", font_size=40, on_release=self.solto, on_press=self.apertado)
		# em kivy os eventos são disparados pelo método on
		# on_press se refere a quando o usuário apertar o botão
		# on_release se refere a quando o usuário soltar o botão
		
		# em  nosso programa, on_release acionará um método que vamos implementar com o nome de apertado
		
		self.texto = Label(text="0") # podemos atribuir variáveis às classes, e estamos fazendo exatamente isso 
		# ao acrescentar a palavra self que é a instância da classe, a isto dá-se o nome de variável de instância, isso pode ser 
		# feito em qualquer classe, vc pode criar uma variável que não existe e definir como sendo da propria classe!
		# isto foi feito pela nescessidade de acessar o label para integrarmos ele dentro da função apertado! 
		
		box.add_widget(botao)
		box.add_widget(self.texto)
		
		return box

	def solto(self, botao):
		"""
		nosso método solto será acionado quando o botão passado como párâmetro desta função
		for solto pelo usuário, e executará os comandos a seguir! 
		"""
		botao.text = "Soltei o botão" # este comando muda o nome do próprio botão par Soltei o botão
		self.texto.text = str(int(self.texto.text)+1) # este outro comando muda o texto do label e soma mais 1 ao texto do label
		
	def apertado(self, botao):
		"""
		nosso método apertado será acionado quando o botão passado como párâmetro desta função
		for solto pelo usuário, e executará os comandos a seguir!
		"""
		botao.text = "Apertei o botão" # este comando muda o text do botão quando for apertado pelo usuário!

Roda.title ='Eventos e Variáveis de Instância' # isto muda o nome da janela
Roda.icon = "../dados/imagens/icon.png"
Roda().run()
 
