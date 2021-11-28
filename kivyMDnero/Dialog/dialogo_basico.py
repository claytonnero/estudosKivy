from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog

KV = '''
MDFloatLayout:

    MDFlatButton:
        text: "DIÁLOGO DE ALERTA"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()
'''


class Example(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
            	title="Este é o titulo",
                text="O Que Deseja Fazer?",
                buttons=[
                    MDFlatButton(
                        text="CANCELAR", text_color=self.theme_cls.primary_color
                    ),
                    MDRaisedButton(
                        text="DESCARTAR", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()


Example().run()