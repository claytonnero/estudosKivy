from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
 
from jnius import autoclass
from time import sleep

class Roda(BoxLayout):
    
    def apertado(self, botao):
        #self.ids.lab.text = "Iniciando"
        # get the MediaPlayer java class
        mPlayer = autoclass('android.media.MediaPlayer')        
        # create our player
        
        mPlayer.setDataSource('time.mp3')
        mPlayer.prepare()
        
        # play
        print ('duration:', mPlayer.getDuration())
        mPlayer.start()
        print ('current position:', mPlayer.getCurrentPosition())
        sleep(50)
        
        # then after the play:
        mPlayer.release()
        self.ids.lab.text = "Terminado"

class App(App):
    def build(self):
        return Roda()

App().run()