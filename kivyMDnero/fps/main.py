KV = '''
Screen:

    MDLabel:
        text: "Hello, World!"
        halign: "center"
'''

from kivy.lang import Builder

from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        """
        cores disponiveis
        ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        matrizes disponiveis 
        ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900', 'A100', 'A200', 'A400', 'A700']
        """
        self.theme_cls.primary_palette = "Âmber"
        
        return Builder.load_string(KV)

    def on_start(self):
        self.fps_monitor_start()


MainApp().run()