#MDCheckbox
from kivy.lang import Builder

from kivymd.app import MDApp


KV = '''
MDFloatLayout:

    MDCheckbox:
        on_active: app.checkboxAtivo(*args)
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .5, 'center_y': .5}
'''


class Test(MDApp):
    
    def checkboxAtivo(self, checkbox, value):
	    if value:
	        print('Desligado', checkbox.state, 'state')
	    else:
	        print('Ligado', checkbox.state, 'state')
        
    def build(self):
        return Builder.load_string(KV)


Test().run()
