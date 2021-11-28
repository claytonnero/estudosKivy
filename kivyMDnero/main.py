from kivymd.app import MDApp
from kivy.lang import Builder

kv = """
MDFloatLayout:
	MDIconButton:
		icon: 'language-python'
		user_font_size: '80dp'
		pos_hint:{'center_x':.5, 'center_y':.8}
	MDTextField:
		hint_text: 'Email::'
		pos_hint:{'center_x':.5, 'center_y':.6}
		size_hint_x:.9
	MDTextField:
		hint_text: 'Senha::'
		pos_hint:{'center_x':.5, 'center_y':.5}
		size_hint_x:.9
	MDRaisedButton:
		pos_hint:{'center_x':.5, 'center_y':.4}
		size_hint_x:.9
		text:'Login'
	MDLabel:
		theme_text_color: "Custom"
		text_color:1,1,1,1
		text:'Esqueceu sua senha??'
		halign:'center'
		pos_hint:{'center_y':.3}
	MDTextButton:
		text:'Clique aqui!'
		pos_hint:{'center_x':.5, 'center_y':.2}
		
"""

class Roda(MDApp):
	def build(self):
		self.theme_cls.primary_palete = 'Green'
		self.theme_cls.acent_palete = "Teal"
		self.theme_cls.theme_style = "Dark"
		return Builder.load_string(kv)
				
Roda().run()