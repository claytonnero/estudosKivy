from os import path
from PIL import Image, ImageEnhance

class Editor():
    img = None
    img_formato = None
    img_local = None
    img_nome = None
    img_ext = None
    
    def girar_imagem(self, sentido="horario", angulo=90):
        
        if (sentido == "horario"):
            self.img = self.img.rotate(angulo * -1, expand=True)
            
        elif (sentido == "anti_horario"):
            self.img = self.img.rotate(angulo, expand=True)
            
    def resetar(self):
        self.img = None
        self.img_formato = None
        self.img_local = None
        self.img_nome = None
        self.img_ext = None
    
    def carregar_imagem(self, imagem):
        try:
            self.img = Image.open(imagem)
            self.img_formato = self.img.format
            self.img_local = path.dirname(path.realpath(imagem))
            self.img_nome, self.img_ext = path.splitext(path.basename(imagem))
            print("Imagem carregada com sucesso!")
            return True
        
        except:
            print("Falha ao carregar imagem!")
            return False
    
    def remover_cor_imagem(self):
        conversor = ImageEnhance.Color(self.img)
        self.img = conversor.enhance(0)
        ##nota** o valor de conversor.enhance() se for 0 nao conterá cor alguma, se for 1 terá a cor normal , se for acima se 1 saturará a imagem e se for negativo (-1) inverterá as cores da imagem
    
    def salvar(self, local, nome_imagem):
        ln = local + "/" + nome_imagem + self.img_ext
        self.img.save(ln, self.img_formato)
        self.resetar()
        
ed = Editor()