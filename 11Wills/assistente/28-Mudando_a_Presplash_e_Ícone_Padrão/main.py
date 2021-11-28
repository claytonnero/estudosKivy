#! /usr/bin/env python3
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class Roda(App):

    def build(self):
        lay = AnchorLayout(anchor_x='center', anchor_y='bottom')
        botao = Button(text='Aperte', size_hint=(None, None))
        lay.add_widget(botao)
        return lay

Roda.title='Mudando a presplash e icone padão'
Roda.icon='../dados/imagens/icon.png'
Roda().run()
