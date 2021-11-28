#https://kivymd.readthedocs.io/en/latest/components/taptargetview/

from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.taptargetview import MDTapTargetView

KV = '''
Screen:

    MDFloatingActionButton:
        id: button
        icon: "plus"
        pos: 10, 10
        on_release: app.tap_target_start()
'''


class TapTargetViewDemo(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        self.tap_target_view = MDTapTargetView(
        
        	#muda a cor do circulo!
        	outer_circle_color=(1, 0, 0),
        	outer_circle_alpha = 2,
        	target_circle_color=(0, 0, 0),
        	
        	draw_shadow=True,
            widget=screen.ids.button,
            title_text="Este é o botao adicionar!",
            description_text="Esta é a descrição do botao!!",
            widget_position="left_bottom",
        )

        return screen

    def tap_target_start(self):
        
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()


TapTargetViewDemo().run()