from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from caronas.auxiliares.resumo_caronas import resumoCaronas
from time import sleep
import os

def caronasUsuarios(caronas_cadastradas, usuarios_cadastrados, usuario_atual):
    print(BANCO_DE_FRASES['titulo_suas_caronas'])
    encontrado_carona = False

    for carona in caronas_cadastradas:
        if carona['usuario_atual'] == usuario_atual:
            encontrado_carona = True
            resumoCaronas(caronas_cadastradas, usuarios_cadastrados)
    os.system("cls" if os.name == 'nt' else 'clear')
    if encontrado_carona == False:
        print(f"{BANCO_DE_FRASES['nenhuma_carona']} \n".center(70))
        sleep(3)
        os.system("cls" if os.name == 'nt' else 'clear')