from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
Screen:

    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "MDLabel"

        MDLabel:
            text: "MDLabel"
        
        MDLabel:
    		text: "MDLabel"
    		halign: "center"
    	
    	MDLabel:
    		text: "Custom color"
    		halign: "center"
    		theme_text_color: "Custom"
    		text_color: 0, 0, 1, 1
    		
    	MDIcon:
    		halign: "center"
    		icon: "android"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()