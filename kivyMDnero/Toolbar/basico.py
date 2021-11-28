from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

kv = """
<Box>:
	orientation:"vertical"
	MDBoxLayout:
		orientation:"vertical"
		MDToolbar:
			id:bar
			specific_text_color: app.theme_cls.accent_dark
			elevation:10
			title:"Barra de Menu"
			
			left_action_items: [["menu", lambda x: x]]
			#right_action_items: [["dots-vertical", lambda x: ]]
						
		MDLabel:
			#md_bg_color:app.theme_cls.accent_light
			text:"deu certo"
			halign:"center"
"""
class Box(BoxLayout):
	
	Builder.load_string(kv)
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)	
			
	def chamada(self):
		self.ids.bar.title = "Mudei no menu"
	
	def chamada2(self):
		self.ids.bar.title = "Mudei no dots-vertical"
		
class Roda(MDApp):	
		
	def build(self):
		return Box()
				
Roda().run()