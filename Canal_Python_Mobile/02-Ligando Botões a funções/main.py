from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

import time

class OlaMundo(BoxLayout):
    def __init__(self, **kwargs):
        super(OlaMundo, self).__init__(**kwargs)
        botão1 = Button(text='Olá')
        botão1.bind(on_press=self.olah)
        self.add_widget(botão1)

        botão2 = Button(text='Mundo!')
        botão2.bind(on_press=self.mundo)
        self.add_widget(botão2)

    def olah(self, obj):
        print('--> Olá Apertado às %s' % time.ctime())

    def mundo(self, obj):
        print('--> Mundo Apertado às %s'% time.ctime())

class Roda(App):
    def build(self):
        return OlaMundo()

if __name__ == '__main__':
    app = Roda()
    print('O nome da Aplicação é {}'.format(app.name))
    app.title = 'Ligando Funções a Botões'
    app.run()
