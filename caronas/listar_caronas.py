import os
from time import sleep
from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from caronas.auxiliares.resumo_caronas import resumoCaronas

def listarCaronas(caronas_cadastradas, usuarios_cadastrados):
    print(BANCO_DE_FRASES['titulo_caronas_disponiveis'] + "\n")
    if(len(caronas_cadastradas) == 0):
        print(f"{BANCO_DE_FRASES['sem_caronas']} \n".center(70))
        sleep(3)
        os.system("cls" if os.name == 'nt' else 'clear')

    else:
        resumoCaronas(caronas_cadastradas, usuarios_cadastrados)
        os.system("cls" if os.name == 'nt' else 'clear')