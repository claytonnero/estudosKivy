from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDFloatLayout:
	MDSwitch:
	    width:dp(10)
        pos_hint: {'center_x': .5, 'center_y': .8}

    MDSwitch:
        pos_hint: {'center_x': .5, 'center_y': .5}
    
    MDSwitch:
        width: dp(64)
        pos_hint: {'center_x': .5, 'center_y': .4}
    
    MDSwitch:
        width: dp(130)
        pos_hint: {'center_x': .5, 'center_y': .3}
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()