import os
from time import sleep
from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from caronas.auxiliares.resumo_caronas import resumoCaronas

def buscarCaronas(caronas_cadastradas, usuarios_cadastrados):
    print(BANCO_DE_FRASES['titulo_busca'])
    while True:      
        origem_busca = input(f"\n{BANCO_DE_FRASES['origem_busca']}").title()
        if origem_busca.strip() == "":
            print(BANCO_DE_FRASES['digite_algo'])
            continue
        elif origem_busca.isnumeric() or origem_busca.isdecimal():
            print(BANCO_DE_FRASES['apenas_letras'])
            continue
        break
    while True:
        destino_busca = input(f"\n{BANCO_DE_FRASES['destino_busca']}").title()
        if destino_busca.strip() == "":
            print(BANCO_DE_FRASES['digite_algo'])
            continue
        elif destino_busca.isnumeric() or destino_busca.isdecimal():
            print(BANCO_DE_FRASES['apenas_letras'])
            continue
        break
    print("\n")
    
    encontrado_carona = False

    for carona in caronas_cadastradas:
        if origem_busca == carona['origem'] and destino_busca == carona['destino']:
            encontrado_carona = True
            resumoCaronas(caronas_cadastradas, usuarios_cadastrados)
    os.system("cls" if os.name == 'nt' else 'clear')

    if encontrado_carona == False:
        print(f"{BANCO_DE_FRASES['nenhuma_carona']} \n".center(70))
        sleep(3)
        os.system("cls" if os.name == 'nt' else 'clear')