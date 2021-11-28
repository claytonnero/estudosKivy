from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.window import Window
from jnius import autoclass
# We need a reference to the Java activity running the current
# application, this reference is stored automatically by
# Kivy's PythonActivity bootstrap

# This one works with SDL2
Window.clearcolor =0.9,1,1,1
class Roda(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def solto(self, botao):
        
        PythonActivity = autoclass('org.kivy.android.PythonActivity')

        activity = PythonActivity.mActivity

        Context = autoclass('android.content.Context')
        vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)
        
        ent = self.ids.ent.text
        if ent == "":
            ent = 50
        vibrator.vibrate(int(ent)) 
        Window.clearcolor = 0,1,0,1
class Vibrate(App):
    def build(self):
        return Roda()
        
Vibrate().run()