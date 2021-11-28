from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import time

class MinhaCaixa(BoxLayout):
    def Olah(self, *args):
        print('--> Olá apertado às %s' % time.ctime())        
        return
    def Mundo(self, *args):
        print('--> Mundo Apertado às %s' % time.ctime())
        return
class Roda(App):
    def build(self):
        return MinhaCaixa()

if __name__ == '__main__':
    app = Roda()
    print('O nome da Aplicação é %s'% app.name)
    app.run()
    
