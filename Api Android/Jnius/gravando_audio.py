from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from jnius import autoclass
from time import sleep

class Rodando(BoxLayout):
    
    def apertado(self, botao):

        # get the needed Java classes
        self.ids.lab.text = "Gravando"
        
        MediaRecorder = autoclass('android.media.MediaRecorder')
        AudioSource = autoclass('android.media.MediaRecorder$AudioSource')
        OutputFormat = autoclass('android.media.MediaRecorder$OutputFormat')
        AudioEncoder = autoclass('android.media.MediaRecorder$AudioEncoder')
        
        # create out recorder
        mRecorder = MediaRecorder()
        mRecorder.setAudioSource(AudioSource.MIC)
        mRecorder.setOutputFormat(OutputFormat.THREE_GPP)
        mRecorder.setOutputFile('testrecorder.3gp')
        mRecorder.setAudioEncoder(AudioEncoder.AMR_NB)
        mRecorder.prepare()
        
        # record 5 seconds
        mRecorder.start()
        sleep(10)
        mRecorder.stop()
        mRecorder.release()
        
        self.ids.lab.text = "Terminado"
        
class App(App):
    def build(self):
        return Rodando()

App().run()               