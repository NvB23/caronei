import os
def fecharPrograma(imagens_pix):
        for imagem in imagens_pix:
            os.remove(imagem)
        os.system("cls" if os.name == 'nt' else 'clear')