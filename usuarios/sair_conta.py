from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
import os
from time import sleep

def sairConta(logado):
    logado = False
    print(BANCO_DE_FRASES['saindo_conta'])
    sleep(2)
    print(BANCO_DE_FRASES['conta_saiu'])
    sleep(1)
    os.system("cls" if os.name == 'nt' else 'clear')
    return logado