#! /usr/bin/env python3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.animation import Animation
import json
from kivy.core.audio import SoundLoader

class Gerenciador(ScreenManager):
	pass

class Menu(Screen):

    def on_pre_enter(self):
        Window.bind(on_request_close=self.confirmacao)

    def confirmacao(self, *args, **kwargs):

        global popupSound
        popupSound.play()
        
        box = BoxLayout(orientation='vertical', padding='20sp', spacing='10sp')
        botoes = BoxLayout(padding='20sp', spacing='10sp')

        pop = Popup(title='Deseja mesmo sair?', content=box, size_hint=(None, None),
                    size=('80dp', '100dp'))

        sim = Botao(text='Sim', on_release=App.get_running_app().stop)        
        nao = Botao(text='Não',  on_release=pop.dismiss)
        
        botoes.add_widget(sim)
        botoes.add_widget(nao)
        
        atencao = Image(source='../dados/imagens/atencao.png')

        box.add_widget(atencao)
        box.add_widget(botoes)

        anim_texto= Animation(duration=0.1, color=(0,0,0,1)) + Animation(color=(1,0,0,1))
        anim_texto.repeat=True
        anim_texto.start(nao)

        anim = Animation(size=(500, 450), duration=0.5, t='out_back')
        anim.start(pop)

        pop.open()
        return True

class Botao(ButtonBehavior,Label):

    cor = ListProperty([0.1,0.5,0.7,1])
    cor2 = ListProperty([0.1,0.1,0.1,1])

    def __init__(self, **kwargs):
        super(Botao,self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def on_press(self, *args):
        self.cor, self.cor2 = self.cor2, self.cor

    def on_cor(self, *args):
        self.atualizar()

    def on_release(self, *args):
        self.cor, self.cor2 = self.cor2, self.cor

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor)
            Ellipse(pos=self.pos, size=(self.height ,self.height ))
            Ellipse(pos=(self.x+self.width-self.height, self.y), size=(self.height,self.height))
            Rectangle(pos=(self.x+self.height/2.0, self.y), size=(self.width-self.height, self.height))

class Fazendo(Screen):


    tarefas = []
    path = ''

    def on_pre_enter(self):
        self.ids.box.clear_widgets()

        self.path = App.get_running_app().user_data_dir+'/'

        self.loadData()
        Window.bind(on_keyboard=self.voltar)
        for tarefa in self.tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))



    def voltar(self, window, key, *args):#neste caso trata como lista

        if key == 27:
            App.get_running_app().root.current = 'menu'
            #print(key) #mostra as teclas pressionadas
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def loadData(self, *args):
        try:
            with open(self.path+'data.json','r') as data:
                self.tarefas = json.load(data)

        except FileNotFoundError:
            pass

    def savedata(self, *args):
        with open(self.path+'data.json','w') as data:
            json.dump(self.tarefas, data)

    def removeWidget(self, tarefa):

        global remSound
        remSound.play()
        texto = tarefa.ids.label.text
        self.ids.box.remove_widget(tarefa)
        self.tarefas.remove(texto)
        self.savedata()


    def addWidget(self):

        global addSound
        addSound.play()
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ""
        self.tarefas.append(texto)
        self.savedata()

class Tarefa(BoxLayout):

	def __init__(self, text="", **kwargs):
		super().__init__(**kwargs)
		self.ids.label.text = text

class Roda(App):

	def build(self):
		return Gerenciador()

popupSound = SoundLoader.load('../dados/sounds/camera-shutter.mp3')
remSound = SoundLoader.load('../dados/sounds/service-logout.mp3')
addSound = SoundLoader.load('../dados/sounds/service-login.mp3')

Roda.title='Conirmação de Saida'
Roda.icon='../dados/imagens/icon.png'
Roda().run()
