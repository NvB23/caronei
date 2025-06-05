import os
from time import sleep
from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES

def validaVazio(opcao):
    if((opcao.strip()) == "" or (opcao not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "00"])):
        print(BANCO_DE_FRASES['digite_algo'])
        sleep(1)
        os.system("cls" if os.name == 'nt' else 'clear')
        return False
    return True