from kivy.app import App
from kivy.uix.button import Button

class Roda(App):
    def build(self):
        return Button(text="Olá Mundo Aperte")

if __name__ == '__main__':
    app = Roda()
    app.title = "Olá Mundão"
    app.run()
